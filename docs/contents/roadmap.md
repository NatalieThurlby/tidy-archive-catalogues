## Roadmap

The project currently aims to have the following functionality:

1. Enable archivists to search their archives for potential typos/mistakes. Specifically, they will be able to be returned with:
    A. Specific places to check in the archive (e.g. specific reference numbers/codes, and columns)
    for mistakes, particularly for:
        i.  Dates
        ii. Named entities (places, people, and businesses)
    B. Flag inconsistencies in the archive, according to a chosen set of archiving guidelines, for
    example if 'c.', 'c', 'circa' are used to mean approximately, offer one option.
        i. According to national archives guidelines
        ii. According to Theatre Collection guidelines
2. Enable digital humanities researchers to digitally visualise/analyse the collection, by creating
 machine-readable and human-readable (for labels, etc) versions of the following c:
    A. Dates, date ranges, and date uncertainty
    B. Named entities (places, people, and businesses)
 
The output of (2.) should give the data in a useful format to interact with existing python/R libraries. 

For example dates should be in a datetime format, places should be either points in longitude/latitude, or polygonal areas (e.g. in geojson), or easy to convert to. There should be tutorial notebooks, for creating simple visualisations of:
    A. Social networks
    B. Geographical areas
    C. Timelines 
    
Both (1) and (2) should be tested on large archives (e.g. British Library and The National Collection), and smaller ones (e.g. The Theatre Collection, and the Harry Ransom Centre)
