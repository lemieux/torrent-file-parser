import cStringIO
import os

from datetime import datetime

from torrent import bencode


def get_file_content(path):
    with open(path, 'r') as f:
        content = f.read()

    return content


def parsed_torrent(path):
    if not os.path.isfile(path):
        raise Exception('The path provided must be a file.')

    content = get_file_content(path)

    torrent_dict = bencode.decode(content)
    return Torrent(torrent_dict)


def _extract_sha_list(value):
    hashes = []

    pieces_count = len(value) / 20

    stream = cStringIO.StringIO(value)

    for _ in range(0, pieces_count):
        piece = stream.read(20)
        hashes.append(piece)

    return hashes


def _extract_files(info_dict):
    files = []
    hashes = _extract_sha_list(info_dict['pieces'])

    if 'files' in info_dict:
        for i, f in enumerate(info_dict['files']):
            files.append(File(f['path'][0], f['length'], hashes[i]))
    else:
        files.append(File(info_dict['name'], info_dict['length'], hashes[0]))

    return files


class File(object):

    def __init__(self, name, length, checksum):
        self.name = name
        self.length = length
        self.checksum = checksum

    def __repr__(self):
        return 'File(name={0}, length={1}, checksum={2})'\
            .format(self.name, self.length, self.checksum)


class Torrent(object):

    def __init__(self, values):
        self.tracker = values['announce'] if 'announce' in values else None
        self.creation_date = datetime.\
            fromtimestamp(int(values['creation date'])) \
            if 'creation date' in values else None

        self.created_by = values[
            'created by'] if 'created by' in values else None

        self.files = _extract_files(values['info'])

    def __repr__(self):
        return 'Torrent(tracker={0}, creation_by={1}, creation_date={2}, files={3})'\
            .format(self.tracker, self.created_by, self.creation_date, self.files)
