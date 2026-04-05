---
layout: jonbarron
title: My Thoughts
permalink: /thoughts/
---

<table style="width:100%;max-width:800px;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;">
  <tbody>
    <tr>
      <td style="padding:0px">

        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;">
          <tbody>
            <tr>
              <td style="padding:16px">
                <p><a href="/">&larr; Jaeik Kim</a></p>
                <h2>My Thoughts</h2>
              </td>
            </tr>
          </tbody>
        </table>

        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;">
          <tbody>
            {% assign sorted_pages = site.html_pages | sort: "date" | reverse %}

            {% for p in sorted_pages %}
              {% if p.url != "/thoughts/" and p.url contains "/thoughts/" %}
              <tr>
                <td style="padding:16px;border-top:1px solid #ebebeb;">
                  <p style="margin:0 0 4px 0;color:#999;font-size:13px;">
                    {{ p.date | date: "%Y-%m-%d" }}
                  </p>
                  <p style="margin:0 0 6px 0;">
                    <strong><a href="{{ p.url }}">{{ p.title }}</a></strong>
                  </p>
                  <p style="margin:0;">
                    {{ p.description }}
                  </p>
                </td>
              </tr>
              {% endif %}
            {% endfor %}
          </tbody>
        </table>

      </td>
    </tr>
  </tbody>
</table>