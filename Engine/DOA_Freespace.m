function Loc_m = DOA_Freespace()
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
 % load Ture_LOSDOA.txt; %载入真实LOS的DOA
 TagID = 1
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
         Phase(TagID,p)=mean(Tem(:,1));       % 获取相位
         RSS(TagID,p)=mean(Tem(:,2));         % 获取RSS
         % 计算复信号
         S(TagID,p)=Rss2amp(RSS(TagID,p))*exp(i*Phase(TagID,p));
 end
 for k=1:K
         y=S(k,:);
         [theta,Pd]=Music(y',Lamuda,Xd,ws);
         [pks,Loc_m] = findpeaks(Pd);
         Loc_m=Loc_m*ws; 
 %         DOALos=Ture_LOSDOA(k,1);
 %         E_DOA(k)=[min(abs(Loc_m-DOALos))];
 end
 % Save2txt(E_DOA,'E_DOA.txt')