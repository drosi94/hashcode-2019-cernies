import file_parser

lines = file_parser.read_file("input/a_example.txt")
total_photos = lines[0]
photos_list = lines[1:]
print(total_photos)
i = 0
photos = {}
for photo in photos_list:
    line = photo.split(' ')
    photo_id = i
    photo_type = line[0]
    total_tags = int(line[1])
    tags = line[2:]
    print(photo_id)
    print(photo_type)
    print(tags)
    photos[photo_id] = [photo_type, tags]
    i += 1
print(photos)
