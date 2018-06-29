import tflearn

from tflearn.datasets import titanic
titanic.download_dataset("titanic_dataset.csv")

from tflearn.data_utils import load_csv
data, labels = load_csv("titanic_dataset.csv", target_column=0, categorical_labels=True,
                        n_classes=2, columns_to_ignore=[2, 7])

for p in data:
    if p[1] == "female":
        p[1] = 1
    else:
        p[1] = 0

# train

net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.fit(data, labels, n_epoch=100, batch_size=16, show_metric=True)

# predict leonardo dicaprio's chance of survival

dicaprio = [3, "Jack", "male", 19, 0, 0, "N/A", 5.0000]

pred = ((model.predict([[3, 0, 19, 0, 0, 5.0]]))[0][1])*100
print(" ")
print("chance of survival: ")
print(pred)
print("out of 100")
print(" ")

# calculate average ticket fare

# total = 0
# for p in data:
#     price = float(p[5])
#     total = total + price
# num_tickets = len(data)
#
# print(total/num_tickets)

