from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape

ppt_path = r"d:\219\NAYARA_Project_Presentation.pptx"
slides = [
    ("NAYARA", "Custom Bag Store Mini-Project", ["Responsive storefront", "Customized bag design", "Live product preview", "Shopping cart and checkout"]),
    ("Key Features", "A complete customer shopping experience", ["Bag type, color, and size selection", "Personalized text, font, and image upload", "Design placement controls", "Order details and checkout"]),
    ("Technology Stack", "Simple and lightweight web development", ["HTML5 structure", "CSS3 responsive styling", "JavaScript interactivity", "Local Ollama AI integration"]),
    ("Local AI Assistant", "llama3.2:latest", ["Chat completed through localhost:11434", "Uses the Ollama /api/chat endpoint", "Provides concise point-based answers", "Requires Ollama and the selected model"]),
]

slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:cSld><p:spTree>
<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
<p:sp><p:nvSpPr><p:cNvPr id="2" name="Title 1"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="274300"/><a:ext cx="11000000" cy="900000"/></a:xfrm><a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="7A5AD2"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="3000" b="1"/><a:t>{title}</a:t></a:r><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>
<p:sp><p:nvSpPr><p:cNvPr id="3" name="Subtitle"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="457200" y="1220000"/><a:ext cx="11000000" cy="500000"/></a:xfrm><a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" sz="1700" i="1"/><a:t>{subtitle}</a:t></a:r><a:endParaRPr lang="en-US" sz="1700"/></a:p></p:txBody></p:sp>
{bullets}
</p:spTree></p:cSld><p:clrMapOvr><a:clrSchemeMapping/></p:clrMapOvr></p:sld>
"""

bullet_xml = """<p:sp><p:nvSpPr><p:cNvPr id="{id}" name="Bullet {n}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="609600" y="{y}"/><a:ext cx="10300000" cy="400000"/></a:xfrm><a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr wrap="square" anchor="ctr"/><a:lstStyle/><a:p><a:pPr marL="342900" indent="-228600"/><a:r><a:rPr lang="en-US" sz="1500"/><a:t>{text}</a:t></a:r><a:endParaRPr lang="en-US" sz="1500"/></a:p></p:txBody></p:sp>"""

content = {
    "[Content_Types].xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>""",
    "_rels/.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>""",
    "docProps/core.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>NAYARA Project Presentation</dc:title><dc:creator>GitHub Copilot</dc:creator><cp:lastModifiedBy>GitHub Copilot</cp:lastModifiedBy><dcterms:created xsi:type="dcterms:W3CDTF">2026-10-08T00:00:00Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2026-10-08T00:00:00Z</dcterms:modified>
</cp:coreProperties>""",
    "docProps/app.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>Microsoft Office PowerPoint</Application><PresentationFormat>On-screen Show (16:9)</PresentationFormat><Slides>4</Slides><Notes>0</Notes><HiddenSlides>0</HiddenSlides><MMClips>0</MMClips><Company>NAYARA</Company><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc><HyperlinksChanged>false</HyperlinksChanged><AppVersion>16.0000</AppVersion></Properties>""",
    "ppt/presentation.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" saveSubsetFonts="1" autoCompressPictures="1"><p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst><p:sldIdLst><p:sldId id="256" r:id="rId2"/><p:sldId id="257" r:id="rId3"/><p:sldId id="258" r:id="rId4"/><p:sldId id="259" r:id="rId5"/></p:sldIdLst><p:sldSz cx="12192000" cy="6858000" type="screen16x9"/><p:notesSz cx="6858000" cy="9144000"/></p:presentation>""",
    "ppt/_rels/presentation.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide2.xml"/><Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide3.xml"/><Relationship Id="rId5" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide4.xml"/></Relationships>""",
    "ppt/slideMasters/slideMaster1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld name="NAYARA Master"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMap><a:schemeClr val="accent1"/><a:schemeClr val="accent2"/><a:schemeClr val="accent3"/><a:schemeClr val="accent4"/><a:schemeClr val="accent5"/><a:schemeClr val="accent6"/><a:schemeClr val="hlink"/><a:schemeClr val="folHlink"/></p:clrMap><p:sldLayoutIdLst><p:sldLayoutId id="1" r:id="rId1"/></p:sldLayoutIdLst></p:sldMaster>""",
    "ppt/slideMasters/_rels/slideMaster1.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>""",
    "ppt/slideLayouts/slideLayout1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1"><p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld><p:clrMapOvr><a:clrSchemeMapping/></p:clrMapOvr></p:sldLayout>""",
    "ppt/theme/theme1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="NAYARA"><a:themeElements><a:clrScheme name="NAYARA"><a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="1C1D2A"/></a:dk2><a:lt2><a:srgbClr val="FFF9F4"/></a:lt2><a:accent1><a:srgbClr val="7A5AD2"/></a:accent1><a:accent2><a:srgbClr val="FF7C7C"/></a:accent2><a:accent3><a:srgbClr val="5AC8AE"/></a:accent3><a:accent4><a:srgbClr val="F5A97D"/></a:accent4><a:accent5><a:srgbClr val="F7D3BF"/></a:accent5><a:accent6><a:srgbClr val="D8C3EE"/></a:accent6><a:hlink><a:srgbClr val="7A5AD2"/></a:hlink><a:folHlink><a:srgbClr val="FF7C7C"/></a:folHlink></a:clrScheme><a:fontScheme name="NAYARA"><a:majorFont><a:latin typeface="Aptos Display"/><a:ea/><a:cs/></a:majorFont><a:minorFont><a:latin typeface="Aptos"/><a:ea/><a:cs/></a:minorFont></a:fontScheme><a:fmtScheme name="NAYARA"><a:fillStyleLst><a:solidFill><a:schemeClr val="accent1"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="12700"><a:solidFill><a:schemeClr val="accent1"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="lt1"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme></a:themeElements></a:theme>""",
}

for index, (title, subtitle, items) in enumerate(slides, 1):
    list_xml = []
    for item_number, item in enumerate(items, 1):
        y = 240000 + item_number * 600000
        list_xml.append(bullet_xml.format(id=item_number + 3, n=item_number, y=y, text=escape(item)))
    content[f"ppt/slides/slide{index}.xml"] = slide_xml.format(title=escape(title), subtitle=escape(subtitle), bullets="".join(list_xml))
    content[f"ppt/slides/_rels/slide{index}.xml.rels"] = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>"""

with ZipFile(ppt_path, "w", ZIP_DEFLATED) as ppt:
    for name, payload in content.items():
        ppt.writestr(name, payload)

print(f"Created {ppt_path}")
