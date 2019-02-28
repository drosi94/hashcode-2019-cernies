import file_parser

lines = file_parser.read_file("input/c_memorable_moments.txt")
total_photos = lines[0]
photos_list = lines[1:]
i = 0
photos_h = {}
photos_v = {}
for photo in photos_list:
    line = photo.split(' ')
    photo_id = i
    photo_type = line[0]
    total_tags = int(line[1])
    tags = line[2:]
    if photo_type == 'V':
        photos_v[photo_id] = [photo_type, tags]
    else:
        photos_h[photo_id] = [photo_type, tags]

    i += 1

slideshow = {}

k = 0
photos_combs = {}
for pid, p in photos_v.items():
    for pid2, p2 in photos_v.items():
        if pid != pid2:
            photos_combs[(pid, pid2)] = ['V', p[1] + list(set(p2[1]) - set(p[1]))]

all_photos = {**photos_h, **photos_combs}
print(all_photos)
for pid, p in all_photos:
    max_comb = -1
    for pid2, p2 in all_photos:
