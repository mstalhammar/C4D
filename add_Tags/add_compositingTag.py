"""
Add compositing tags from outside the tags-submenues

Written for Cinema 4D R18.048

Name-US: Add Compositing-Tag
Description-US: Add Compositing-Tag to selected object 
"""

import c4d


def main():
    doc = c4d.documents.GetActiveDocument()
    selected = doc.GetActiveObjects(0)
    if not selected:
        return

    t_i_d = 5637  # Tag-ID goes here

    doc.StartUndo()
    for obj in selected:
        v = []  # Initiate list for all tag IDs
        t = obj.GetTags()  # Get all tags from object
        if t is not None:  # If already Tags found -> do Checks
            for i in t:  # Extract Tag IDs from all tags
                i = str(str(i).strip()).split()
                v.append(i[6])  # Save all tag IDs to v
            if str(t_i_d) in v:  # check if one tag is Portection tag already
                pass  # if yes, move onto nex object
            else:
                tag = obj.MakeTag(t_i_d)  # create + add protection tag
                tag.SetBit(c4d.BIT_ACTIVE)  # set tag active in attr.manager
                doc.AddUndo(c4d.UNDOTYPE_NEW, tag)
    doc.EndUndo()
    c4d.EventAdd()


if __name__ == '__main__':
    main()
