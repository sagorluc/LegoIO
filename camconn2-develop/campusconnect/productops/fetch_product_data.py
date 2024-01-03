def count_services(MODEL_PRODUCT):
    total_num_services = MODEL_PRODUCT.objects.all().count()
    return total_num_services


def get_category(id,MODEL_PRODUCT,MODEL_PRODUCT_CAT):
    cat_selected = MODEL_PRODUCT.objects.filter(id=id).values_list('category', flat=True).first()
    cat_selected = MODEL_PRODUCT_CAT.objects.filter(id=cat_selected)
    return cat_selected


def get_cat_list(id,MODEL_PRODUCT, MODEL_PRODUCT_CAT):
    cat_selected = MODEL_PRODUCT.objects.filter(id=id).values_list('category', flat=True).first()
    cat_list = MODEL_PRODUCT_CAT.objects.all().exclude(id=cat_selected)
    return cat_list


def get_other_services(id,MODEL_PRODUCT):
    cat_selected = MODEL_PRODUCT.objects.filter(id=id).values_list('category', flat=True).first()
    serv_others  = MODEL_PRODUCT.objects.all().exclude(id=id).filter(category=cat_selected)
    return serv_others


# cat_selected = MODEL_PRODUCT.objects.filter(id=id).values_list('category', flat=True).first()
# cat_list     = MODEL_PRODUCT_CAT.objects.all().exclude(id=cat_selected)
# serv_others  = MODEL_PRODUCT.objects.all().exclude(id=id).filter(category=cat_selected)


# def get_category_v0(id,MODEL_PRODUCT,MODEL_PRODUCT_CAT):
#     cat_selected = MODEL_PRODUCT.objects.filter(id=id).values_list('category', flat=True).first()
#     if MODEL_PRODUCT:
#         cat_selected = MODEL_PRODUCT #MODEL_PRODUCT_CAT.objects.filter(id=id).values_list('tagname', flat=True).first()
#         # cat_selected = MODEL_PRODUCT_CAT.objects.filter(id=id).values_list('tagname', flat=True).first()
#     else:
#         cat_selected = 'no model selected'
#         # cat_selected = MODEL_PRODUCT_CAT.objects.filter(id=cat_selected).values_list('tagname', flat=True).first()
#     return cat_selected
