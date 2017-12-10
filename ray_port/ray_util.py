import tensorflow as tf
import pickle

def flags_serializer(flags):
    return pickle.dumps(flags.__dict__)

def flags_deserializer(s):
    flags = tf.app.flags.FLAGS
    flags.__dict__ = pickle.loads(s)
    return flags
