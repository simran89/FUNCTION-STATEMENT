import matplotlib.pyplot as plt
x=[0,2,4,6,8]
y=[0,4,16,36,64]
fig, ax = plt.subplots()
ax.scatter(x,y, marker='o')
ax.set_title("basic components of matplotlib figure")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")

ax.legend()
plt.show()