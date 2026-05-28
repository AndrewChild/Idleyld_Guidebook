import sys
import time
sys.path.insert(1, '../LocalBoulders')
from data.GB_Book import book
from data.GB_Main import *
from images.GB_Images import *


if __name__ == '__main__':
    # Record the start time
    start_time = time.perf_counter()
    book.file_name = 'Idleyld_guidebook'
    book.update()
    book.gen()

    with open('missing_info.txt', 'w') as f:
        f.write('----Formations with no gps----\n')
        for formation in book.formations.values():
            if not formation.gps and formation.name:
                f.write(formation.name+'\n')

        f.write('\n----climbs with no description----\n')
        for climb in book.climbs.values():
            if not climb.description or 'PLACEHOLDER' in climb.description:
                f.write(climb.name+'\n')

        f.write('\n----climbs with no rating----\n')
        for climb in book.climbs.values():
            if climb.rating == -1 and 'Project' not in climb.name:
                f.write(climb.name+'\n')

        f.write('\n----climbs with no topo----\n')
        for climb in book.climbs.values():
            if not climb.hasTopo:
                f.write(climb.name+'\n')

        f.write('\n----climbs with no FA info----\n')
        for climb in book.climbs.values():
            if not climb.FA:
                f.write(climb.name+'\n')

    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")