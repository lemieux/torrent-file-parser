import torrent
import sys


def main(path):
    print torrent.parsed_torrent(path)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        raise Exception('You must provide a path to a torrent file.')
    else:
        main(args[0])
