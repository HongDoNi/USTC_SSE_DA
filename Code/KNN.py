import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report #��������,��ͳ���е��������

data_tr = pd.read_csv('iris_tr.csv')
data_te = pd.read_csv('iris_te.csv')
labels = data_te['class']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(data_tr.iloc[:, :-1], data_tr.iloc[:, -1])
pre = knn.predict(data_te.iloc[:, :-1])
pre == labels

confusion_matrix(labels,pre)#3*3������Ϊ��3���ǩ
report = classification_report(labels,pre)#���౨��,׼ȷ�ʣ��ٻ��ʣ�f1ϵ����ʵ�ʸ��������һ��������������ֵ���ܸ���
print(report)
