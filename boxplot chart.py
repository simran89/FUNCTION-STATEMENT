import matplotlib.pyplot as plt
data=[[10,12,14,15,18,20,22],
[8,9,11,13,17,19,21] ,
[14,16,18,20,23,25,27]]
plt.boxplot(data)
plt.xlabel("groups")
plt.ylabel("values")
plt.title("box plot")
plt.show()