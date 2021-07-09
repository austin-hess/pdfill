import sys
from pdfformfields import fill_form_fields, generate_dictionary

input_filename = sys.argv[1]
output_filename = sys.argv[2]

form_fields = {
    "topmostSubform[0].Page1[0].f_1[0]": "Austin Hess",
    "topmostSubform[0].Page1[0].f_2[0]": "USA",
    "topmostSubform[0].Page1[0].f_3[0]": "",
    "topmostSubform[0].Page1[0].f_4[0]": "",
    "topmostSubform[0].Page1[0].f_5[0]": "",
    "topmostSubform[0].Page1[0].f_6[0]": "",
    "topmostSubform[0].Page1[0].f_7[0]": "",
    "topmostSubform[0].Page1[0].f_8[0]": "",
    "topmostSubform[0].Page1[0].f_9[0]": "",
    "topmostSubform[0].Page1[0].f_10[0]": "",
    "topmostSubform[0].Page1[0].f_11[0]": "",
    "topmostSubform[0].Page1[0].f_12[0]": "",
    "topmostSubform[0].Page1[0].f_13[0]": "",
    "topmostSubform[0].Page1[0].f_14[0]": "",
    "topmostSubform[0].Page1[0].f_15[0]": "",
    "topmostSubform[0].Page1[0].f_16[0]": "",
    "topmostSubform[0].Page1[0].f_17[0]": "",
    "topmostSubform[0].Page1[0].f_18[0]": "",
    "topmostSubform[0].Page1[0].f_19[0]": "",
    "topmostSubform[0].Page1[0].f_20[0]": "",
    "topmostSubform[0].Page1[0].Date[0]": "",
    "topmostSubform[0].Page1[0].f_21[0]": "",
    "topmostSubform[0].Page1[0].f_22[0]": "",
    "topmostSubform[0]": "",
}

fill_form_fields(input_filename, form_fields, output_filename)