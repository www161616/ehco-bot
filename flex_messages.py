# -*- coding: utf-8 -*-

# 此檔案專門儲存所有地區分店的 Flex Message JSON 內容

# 台北市分店 JSON (忠順、文山、萬華)
taipei_stores_json = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": { "type": "image", "url": "https://i.meee.com.tw/eqM7D3D.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": {
        "type": "box", "layout": "vertical", "spacing": "md",
        "contents": [
          { "type": "text", "text": "包子媽生鮮小舖 - 忠順店", "weight": "bold", "size": "xl" },
          { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
              { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
                  { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
                  { "type": "text", "text": "台北市文山區忠順街一段6號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
              ]},
              { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
                  { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
                  { "type": "text", "text": "週一至五 11:00-20:00\\\\n週六 11:00-16:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
              ]}
          ]}
        ]
      },
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "style": "primary", "color": "#AAAAAA", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0229393968" }},
            { "type": "button", "style": "primary", "color": "#1DB446", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/AmWZTzE" }}
          ]},
          { "type": "separator", "margin": "md" },
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "style": "link", "height": "sm", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/kwa8FPiLo5A6Ra5b6" }},
            { "type": "button", "style": "link", "height": "sm", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }}
          ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble",
      "hero": { "type": "image", "url": "https://i.meee.com.tw/NPepnrZ.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": {
        "type": "box", "layout": "vertical", "spacing": "md",
        "contents": [
          { "type": "text", "text": "包子媽生鮮小舖 - 文山店", "weight": "bold", "size": "xl" },
          { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
              { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
                  { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
                  { "type": "text", "text": "台北市文山區保儀路26巷4-2號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
              ]},
              { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
                  { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
                  { "type": "text", "text": "週一至五 11:00-20:00\\\\n週六 11:00-16:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
              ]}
          ]}
        ]
      },
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "style": "primary", "color": "#AAAAAA", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0229383188" }},
            { "type": "button", "style": "primary", "color": "#1DB446", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/otXQFg1" }}
          ]},
          { "type": "separator", "margin": "md" },
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "style": "link", "height": "sm", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/g76Fj7K2UyezR3T77" }},
            { "type": "button", "style": "link", "height": "sm", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }}
          ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble",
      "hero": { "type": "image", "url": "https://i.meee.com.tw/R6v36tH.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": {
        "type": "box", "layout": "vertical", "spacing": "md",
        "contents": [
          { "type": "text", "text": "包子媽生鮮小舖 - 萬華店", "weight": "bold", "size": "xl" },
          { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
              { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
                  { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
                  { "type": "text", "text": "台北市萬華區南寧路68號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
              ]},
              { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
                  { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
                  { "type": "text", "text": "週一至日 12:00-21:30", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
              ]}
          ]}
        ]
      },
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "style": "primary", "color": "#AAAAAA", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0223026762" }},
            { "type": "button", "style": "primary", "color": "#1DB446", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/kwZ1flF" }}
          ]},
          { "type": "separator", "margin": "md" },
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "style": "link", "height": "sm", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/qk3witohdAea4m5N9" }},
            { "type": "button", "style": "link", "height": "sm", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }}
          ]}
      ], "flex": 0 }
    }
  ]
}
"""

# 新北市分店 JSON Part 1 (中和、四號公園、三峽、淡水、林口、永和)
new_taipei_stores_json_1 = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/NelSgwA.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 中和店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市中和區景平路456號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 12:00-21:00\\\\n週六 14:00-20:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0222235530" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/d3JRGrU" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/H9c9tnGDAqZc2PGm8" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/R6v36tH.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽 - 四號公園店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市中和區中安街234號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 12:00-21:00\\\\n週六 14:00-21:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0229400005" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/DfciDTz" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/5r1wV2uAWBRvM3St7" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/E8dA4IP.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 三峽店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市樹林區大義路202號1樓", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至六 10:00-20:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0226687133" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/xDjQ7oG" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/H8MXgVPo4TW9DAG18" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/Sn2wdOj.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 淡水店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市淡水區北新路25號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至六 10:30-20:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0913377711" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/vR4zMsU" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/9RXyjEWTYAk9bPKv6" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/Ay05S9J.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 林口店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市林口區文化三路一段447巷37號1樓", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 10:00-20:00\\\\n週六 11:00-18:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0226007719" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/uUHbJ7q" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/yEFKwizaXp5Lv63SA" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/R6v36tH.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 永和店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市永和區福和路229號1樓", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 08:30-20:00\\\\n週六 10:00-17:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0286609695" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/XsHAXP3" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/5ayPy8EGjuubEr297" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    }
  ]
}
"""

# 新北市分店 JSON Part 2 (板橋、泰山、環球)
new_taipei_stores_json_2 = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/oS9yzJN.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 板橋店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市板橋區漢生東路279巷38號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 9:00-19:30\\\\n週六 9:00-12:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0982169858" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/EJHw7tw" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/ZZeveP1wKdfm4iS76" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/w9H4Aq0.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 泰山店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市泰山區民生路12號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至四 09:00-20:00\\\\n週五至六 09:00-19:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0229093979" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/orntlQf" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/1hWwrb2BZMVPutXJA" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/RT2lyST.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 環球店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新北市中和區民享街35巷8弄3號1樓", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至六 12:00-21:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:0222264143" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/kciJD4u" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/1Ws8APtj8vyqefJs5" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    }
  ]
}
"""

# 桃園市分店 JSON (南平、古華、平鎮、經國)
taoyuan_stores_json = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/R6v36tH.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 南平店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "桃園市桃園區南平路479-1號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 11:00-20:00\\\\n週六 11:00-16:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:033586938" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/86psruB" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/cDwuJGbL2uY4zxck9" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/mb4e6OS.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 古華店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "桃園市中壢區三光路323號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 11:00-20:00\\\\n週六 11:00-17:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:034928881" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/1HFIB0J" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/bFrLZeHBvffgrB5M9" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/YVlZvpW.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 平鎮店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "桃園市平鎮區金陵路258號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 10:00-20:00\\\\n週六 10:00-18:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:034287999" }, "style": "primary", "color": "#AAAAAA" },
            { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/WUb3S8Y" }, "style": "primary", "color": "#1DB446" }
          ]},
          { "type": "separator", "margin": "md" },
          { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
            { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/zusFd3oY8stzatpb9" }, "style": "link", "height": "sm" },
            { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
          ]}
      ], "flex": 0 }
    },
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/R6v36tH.jpg", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 經國店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "桃園市桃園區經國路269號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 15:00-20:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:032606100" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/oVqHTln" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/1mYTVLTLYuFXZF8o6" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    }
  ]
}
"""

# 新竹縣分店 JSON (湖口)
hsinchu_stores_json = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble", "hero": { "type": "image", "url": "https://i.meee.com.tw/mvCCfuZ.png", "size": "full", "aspectRatio": "20:13", "aspectMode": "cover" },
      "body": { "type": "box", "layout": "vertical", "contents": [
        { "type": "text", "text": "包子媽生鮮小舖 - 湖口店", "weight": "bold", "size": "xl" },
        { "type": "box", "layout": "vertical", "margin": "lg", "spacing": "sm", "contents": [
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "地址", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "新竹縣湖口鄉民族街59號", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]},
          { "type": "box", "layout": "baseline", "spacing": "sm", "contents": [
            { "type": "text", "text": "時間", "color": "#aaaaaa", "size": "sm", "flex": 1 },
            { "type": "text", "text": "週一至五 09:00-20:00\\\\n週六 10:00-17:00", "wrap": true, "color": "#666666", "size": "sm", "flex": 5 }
          ]}
        ]}
      ]},
      "footer": { "type": "box", "layout": "vertical", "spacing": "sm", "contents": [
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "撥打電話", "uri": "tel:035994549" }, "style": "primary", "color": "#AAAAAA" },
          { "type": "button", "action": { "type": "uri", "label": "加入LINE好友", "uri": "https://lin.ee/iMgK7uk" }, "style": "primary", "color": "#1DB446" }
        ]},
        { "type": "separator", "margin": "md" },
        { "type": "box", "layout": "horizontal", "spacing": "sm", "contents": [
          { "type": "button", "action": { "type": "uri", "label": "地圖導航", "uri": "https://maps.app.goo.gl/DsFxWHXXUtnJWv3p6" }, "style": "link", "height": "sm" },
          { "type": "button", "action": { "type": "message", "label": "重新選擇區域", "text": "門市查詢" }, "style": "link", "height": "sm" }
        ]}
      ], "flex": 0 }
    }
  ]
}
"""

