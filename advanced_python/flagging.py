from absl import flags
from absl import app

flags.DEFINE_integer('Hello', 0, 'HI')

FLAGS = flags.FLAGS


def main(args):
    del args

    print(FLAGS.Hello)


if __name__ == "__main__":
    app.run(main)