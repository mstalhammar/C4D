"""
Add compositing tags from outside the tags-submenues

Written for Cinema 4D R18.048

Name-US: Add Compositing-Tag
Description-US: Add Compositing-Tag to selected object 
"""

import c4d


def main():
    selected = doc.GetActiveObjects(0)
    if not selected: return
    doc.StartUndo()
    doc.SetActiveTag(None, c4d.SELECTION_NEW)
    for obj in selected:
        if obj.GetTag(c4d.Tcompositing) == None:
            tag = obj.MakeTag(c4d.Tcompositing)
            doc.SetActiveTag(tag, c4d.SELECTION_ADD)
            doc.AddUndo(c4d.UNDOTYPE_NEW, tag)

    doc.EndUndo()
    c4d.EventAdd()


if __name__ == '__main__':
    main()
