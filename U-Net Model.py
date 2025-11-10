import tensorflow as tf
from tensorflow.keras import layers, models




def conv_block(inputs, filters):
x = layers.Conv2D(filters, 3, activation='relu', padding='same')(inputs)
x = layers.Conv2D(filters, 3, activation='relu', padding='same')(x)
return x




def encoder_block(inputs, filters):
x = conv_block(inputs, filters)
p = layers.MaxPooling2D((2, 2))(x)
return x, p




def decoder_block(inputs, skip_features, filters):
x = layers.Conv2DTranspose(filters, 2, strides=2, padding='same')(inputs)
x = layers.concatenate([x, skip_features])
x = conv_block(x, filters)
return x




def build_unet(input_shape=(256, 256, 3)):
inputs = layers.Input(input_shape)


s1, p1 = encoder_block(inputs, 64)
s2, p2 = encoder_block(p1, 128)
s3, p3 = encoder_block(p2, 256)
s4, p4 = encoder_block(p3, 512)


b1 = conv_block(p4, 1024)


d1 = decoder_block(b1, s4, 512)
d2 = decoder_block(d1, s3, 256)
d3 = decoder_block(d2, s2, 128)
d4 = decoder_block(d3, s1, 64)


outputs = layers.Conv2D(1, 1, activation='sigmoid')(d4)


model = models.Model(inputs, outputs)
return model