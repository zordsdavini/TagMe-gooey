# -*- coding: utf-8 -*-

"""Main run script."""

from gooey import Gooey, GooeyParser
from TagMe.tag import Tag
from TagMe.command import Command

__version__ = "0.0.1"
# actions = [
#         'add_tag_to_file',
#         'add_tag_to_directory',
#         'remove_tag_from_file',
#         'remove_tag_from_directory',
#         'clean_directory',
#         ]


@Gooey(program_name="TagMe",
       program_description=__version__,
       advanced=True
       )
def main():
    command_manager = Command()

    parser = GooeyParser()
    subs = parser.add_subparsers(help='command', dest='command')

    add_tag_to_file = subs.add_parser('add_tag_to_file',
                                      help='add tags to selected files'
                                      )
    add_tag_to_file.add_argument('files',
                                 help="select files to process",
                                 widget="MultiFileChooser"
                                 )
    add_tag_to_file.add_argument('tags',
                                 help="select tags",
                                 widget='Listbox',
                                 choices=Tag.TAG_LIST,
                                 nargs="*"
                                 )

    add_tag_to_directory = subs.add_parser('add_tag_to_directory',
                                           help='add tags to selected directory recursevly'
                                           )
    add_tag_to_directory.add_argument('directory',
                                      help="select directory to process",
                                      widget="DirChooser"
                                      )
    add_tag_to_directory.add_argument('tags',
                                      help="select tags",
                                      widget='Listbox',
                                      choices=Tag.TAG_LIST,
                                      nargs="*"
                                      )
    remove_tag_from_file = subs.add_parser('remove_tag_from_file',
                                           help='remove tags from selected files'
                                           )
    remove_tag_from_file.add_argument('files',
                                      help="select files to process",
                                      widget="MultiFileChooser"
                                      )
    remove_tag_from_file.add_argument('tags',
                                      help="select tags",
                                      widget='Listbox',
                                      choices=Tag.TAG_LIST,
                                      nargs="*"
                                      )

    remove_tag_from_directory = subs.add_parser('remove_tag_from_directory',
                                                help='add tags to selected directory recursevly'
                                                )
    remove_tag_from_directory.add_argument('directory',
                                           help="select directory to process",
                                           widget="DirChooser"
                                           )
    remove_tag_from_directory.add_argument('tags',
                                           help="select tags",
                                           widget='Listbox',
                                           choices=Tag.TAG_LIST,
                                           nargs="*"
                                           )

    clean_directory = subs.add_parser('clean_directory',
                                      help='remove files from source directory what exists in destination directory'
                                      )
    clean_directory.add_argument('source_directory',
                                 help="select directory to process",
                                 widget="DirChooser"
                                 )
    clean_directory.add_argument('directory',
                                 help="select directory to check",
                                 widget="DirChooser"
                                 )
    args = parser.parse_args()

    if args.command == 'add_tag_to_file':
        print('Adding tag to file...')
        command_manager.process_add_tag_to_file(args.tags, args.files.split(':'))

    elif args.command == 'add_tag_to_directory':
        print('Adding tag to directory...')
        command_manager.process_add_tag_to_directory(args.tags, args.directory)

    elif args.command == 'remove_tag_from_file':
        print('Removing tag to file...')
        command_manager.process_remove_tag_from_file(
                args.tags,
                args.files.split(':'))

    elif args.command == 'remove_tag_from_directory':
        print('Removing tag to directory...')
        command_manager.process_remove_tag_from_directory(
                args.tags,
                args.directory)

    elif args.command == 'clean_directory':
        print('Cleaning directory...')
        command_manager.process_clean_directory(
                args.source_directory,
                args.directory)
