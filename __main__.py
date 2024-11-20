import fitz

input_file = "Resources/handoutPresentation.pdf"
output_file = "actualPresentation.pdf"
doc = fitz.open(input_file)
output_doc = fitz.open()

first_rect = fitz.Rect(42, 108, 286, 246)
second_rect = fitz.Rect(42, 352, 286, 489)
third_rect = fitz.Rect(42, 602, 286, 732)


for page_num in range(len(doc)):
    page = doc[page_num]

    # Crop and add first part of page
    top_slide_page = output_doc.new_page(width=first_rect.width, height=first_rect.height)
    top_slide_page.show_pdf_page(
        rect=fitz.Rect(0, 0, first_rect.width, first_rect.height),
        src=doc,
        clip=first_rect,
        pno=page_num
    )

    # Crop and add second part of page
    bottom_slide_page = output_doc.new_page(width=second_rect.width, height=second_rect.height)
    bottom_slide_page.show_pdf_page(
        rect=fitz.Rect(0, 0, second_rect.width, second_rect.height),
        src=doc,
        clip=second_rect,
        pno=page_num
    )

    # Crop and add second part of page
    bottom_slide_page = output_doc.new_page(width=third_rect.width, height=third_rect.height)
    bottom_slide_page.show_pdf_page(
        rect=fitz.Rect(0, 0, third_rect.width, third_rect.height),
        src=doc,
        clip=third_rect,
        pno=page_num
    )

output_doc.save(output_file)
output_doc.close()
doc.close()
