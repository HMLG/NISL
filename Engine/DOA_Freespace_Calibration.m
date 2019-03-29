function Loc_m=DOA_Freespace_Calibration()
    clc
    clear all
    close all
%% ��������
    Fre=920.875*10^6;
    Lamuda=3*10^8/Fre;
    ds=0.08;  %��Ԫ���
    M=4;        %��Ԫ����
    ws=0.1;
    Xd=0:ds:(M-1)*ds;     %  ��Ԫ��һά����,��������
    K=1;           %Tag����
    Level=10^4;

%% ��������
%load Ture_LOSDOA.txt; %������ʵLOS��DOA

    for TagID=15:15
        foldname=['E:\1\'];
        file=dir([foldname,'*.txt']);
        filename={file.name};
        L=length(filename);
        for p=1:L
        load([foldname,char(filename(p))]); % ��cell����ת��string��
        end
        for p=1:M
            Antenna_name=['Antenna',num2str(p)];
            Tem = eval(Antenna_name);
            Phase(TagID-14,p)=mean(Tem(:,1));       % ��ȡ��λ
            RSS(TagID-14,p)=mean(Tem(:,2));         % ��ȡRSS
        % ���㸴�ź�
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
    En=V(:,indx(Tn+1:n1)); % ������������
    sata=73.080283 % 16������
    a=exp(-i*2*pi*Xd*cos(deg2rad(sata))/Lamuda)';

    %% �Ż�
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
