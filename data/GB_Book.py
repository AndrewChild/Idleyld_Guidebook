from dataStructure.Book import Book


book = Book(
    name='Idleyld',
    collaborators=['Andrew Child', 'Griffin Thoms', 'Silas Thoms'],
    repo='https://andrewchild.github.io/Idleyld_Guidebook/',
    dl='https://github.com/AndrewChild/Idleyld_Guidebook/raw/refs/heads/main/Idleyld_guidebook.pdf',
    paths={
        'LaTeXTemplates': '../LocalBoulders/templates/',
        'LaTeXOut': './sections/',
        'pdf': './',
        'photos': './images/photos/',
        'graphics': './images/maps',
        'histogram_o': './images/maps/plots/',
        'qr_o': './images/maps/qr/',
        'topo_i': './images/maps/topos/',
        'topo_o': './images/maps/topos/',
        'subarea_i': './images/maps/area/',
        'subarea_o': './images/maps/area/out/',
        'area_i': './images/maps/area/',
        'area_o': './images/maps/area/out/',
    },
    special_thanks=[
    ],
    format_options = ['skip_acknowledgments']
)



if __name__ == '__main__':
    sys.exit()
