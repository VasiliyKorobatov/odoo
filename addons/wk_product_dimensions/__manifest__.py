# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Product Dimensions",
  "summary"              :  "Provide Product Dimensions Option for  products.",
  "category"             :  "Website",
  "version"              :  "0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "website"              :  "",
  "description"          :  "",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=wk_product_dimensions&version=10.0",
  "depends"              :  ['product'],
  "data"                 :  ['views/views.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "pre_init_hook"        :  "pre_init_check",
}