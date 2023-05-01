#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
import numpy as np
import tensorflow as tf

# 准备数据
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
output_data = np.array([[0], [1], [1], [0]], dtype=np.float32)

# 定义模型的神经网络
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=2, input_dim=2, activation=tf.nn.relu),
    tf.keras.layers.Dense(units=1, activation=tf.nn.sigmoid)
])

# 编译模型
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 训练模型
model.fit(input_data, output_data, epochs=1000)

# 执行预测
prediction = model.predict(input_data)
print(prediction)
