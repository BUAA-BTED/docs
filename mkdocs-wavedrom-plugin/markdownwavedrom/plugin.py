# Copyright (c) 2019, Shimoda <kuri65536 at hotmail dot com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
from typing import Text
from mkdocs.plugins import BasePlugin  # type: ignore
from bs4 import BeautifulSoup          # type: ignore


class MarkdownWavedromPlugin(BasePlugin):
    def on_post_page(self, output_content, config, **kwargs):
        # type: () -> Text
        soup = BeautifulSoup(output_content, 'html.parser')
        sections = soup.find_all("div", class_="wavedrom")

        f_exists = False
        for section in sections:
            f_exists = True
            # replace code with div
            section.name = "script"
            section["type"] = "WaveDrom"
            # replace <pre>
            section.replace_with(section)

        if f_exists:
            new_tag = soup.new_tag("script")
            new_tag.string = ("window.addEventListener('load', function() {"
                              "WaveDrom.ProcessAll();});")
            soup.find("body").append(new_tag)

        return Text(soup)
