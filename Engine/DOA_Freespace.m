function Loc_m = DOA_Freespace()
 clc
 clear all
 close all
 %% ��������
 Fre=920.875*10^6;
 Lamuda=3*10^8/Fre;
 ds=0.08;  %��Ԫ���
 M=8;        %��Ԫ����
 ws=0.1;
 Xd=0:ds:(M-1)*ds;     %  ��Ԫ��һά����,��������
 K=1;           %Tag����
 Level=10^4;
 %% ��������
 % load Ture_LOSDOA.txt; %������ʵLOS��DOA
 TagID = 1
 foldname=['E:\MUSIC\Data_Free\'];
 file=dir([foldname,'*.txt']);
 filename={file.name};
 L=length(filename);
 for p=1:L
         load([foldname,char(filename(p))]); % ��cell����ת��string��
 end
 for p=1:M
         Antenna_name=['Antenna',num2str(p)];
         Tem = eval(Antenna_name);
         Phase(TagID,p)=mean(Tem(:,1));       % ��ȡ��λ
         RSS(TagID,p)=mean(Tem(:,2));         % ��ȡRSS
         % ���㸴�ź�
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