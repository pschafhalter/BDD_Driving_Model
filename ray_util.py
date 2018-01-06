import pickle
import tensorflow as tf


flags_serialized = None

def serialize_flags():
    global flags_serialized
    FLAGS = tf.app.flags.FLAGS
    FLAGS._parse_flags()
    flags_serialized = pickle.dumps(FLAGS.__flags)


def deserialize_flags():
    FLAGS = tf.app.flags.FLAGS
    attributes = pickle.loads(flags_serialized)
    for k, v in attributes.items():
        setattr(FLAGS, k, v)
    return FLAGS


def reserialize_flags(flags):
    global flags_serialized
    flags_serialized = pickle.dumps(flags.__flags)

