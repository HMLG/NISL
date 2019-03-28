function Loc_m = DOA_Freespace_Calibration()
clc
clear all
close all
%% 阵列设置
Fre=920.875*10^6;
Lamuda=3*10^8/Fre;
ds=0.08;  %阵元间隔
M=8;        %阵元个数
ws=0.1;
Xd=0:ds:(M-1)*ds;     %  阵元的一维坐标,均匀线阵
K=1;           %Tag个数
Level=10^4;

%% 导入数据
%load Ture_LOSDOA.txt; %载入真实LOS的DOA

for TagID=15:15
    foldname=['E:\MUSIC\Data_Free\'];
    file=dir([foldname,'*.txt']);
    filename={file.name};
    L=length(filename);
    for p=1:L
        load([foldname,char(filename(p))]); % 将cell类型转成string型
    end
    for p=1:M
        Antenna_name=['Antenna',num2str(p)];
        Tem = eval(Antenna_name);
        Phase(TagID-14,p)=mean(Tem(:,1));       % 获取相位
        RSS(TagID-14,p)=mean(Tem(:,2));         % 获取RSS
        % 计算复信号
        S(TagID-14,p)=Rss2amp(RSS(TagID-14,p))*exp(i*Phase(TagID-14,p));
    end
end

Lb=-2*pi*ones(1,M-1);
Ub=2*pi*ones(1,M-1);
 for k=1:K

    X=S(k,:)';
    R=X*X';
    [n1,n2]=size(R);
    [V,D]=eig(R);  % R*V=V*D; R=V*D*V' % eigenvalues (D) and eigenvectors (V)
    D_va=diag(D);
    [D_val,indx]=sort(D_va,'descend');    
    if abs(max(D_val)/min(D_val))<Level
        fprintf('Warning: The eigen values are not correct!\n')
        fprintf('The estinated DOAs are wrong!\n')
    end
    Tn=n1-length(find(D_val<max(D_val)/Level));
    txt=['There are Tn=',num2str(Tn),' largest eigen values. \n'];   
    fprintf(txt)
    En=V(:,indx(Tn+1:n1)); % 噪声特征向量
    sata=73.080283 % 16号天线
    a=exp(-i*2*pi*Xd*cos(deg2rad(sata))/Lamuda)';

    %% 优化
    Obj=@(b)real((a.*exp(-i*[0,b]'))'*En*En'*(a.*exp(-i*[0,b]')));
    b0 = ga(Obj,M-1,[],[],[],[],Lb,Ub);
    [b,fval] =fminsearch(Obj,b0) ;
    Ext=[0,b];
    J(k)=real((a.*exp(-i*Ext'))'*En*En'*(a.*exp(-i*Ext')));
    
    %% music
    for t=1:K
       y=S(t,:)';
       y=y.*exp(+i*Ext');
        [theta,Pd]=Music(y,Lamuda,Xd,ws);
%         plot(sata,Pd);
%         hold on
       [pks,Loc_m] = findpeaks(Pd);
        Loc_m=Loc_m*ws; 
        %DOALos=Ture_LOSDOA(t,1);
        %E_DOA(k,t)=[min(abs(Loc_m-DOALos))];
    end
 end
 
 %Save2txt(E_DOA,'E_DOA_calibration.txt')
