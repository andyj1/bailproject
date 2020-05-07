var arkansas = {
  nodes: [
    // ARKANSAS
    { nodeName: "ASIAN", group: 2 },
    { nodeName: "WHITE", group: 2 },
    { nodeName: "BLACK", group: 2 },
    { nodeName: "HISPANIC", group: 2 },
    { nodeName: "INDIAN", group: 2 },
    { nodeName: "OTHER", group: 2 },

    { nodeName: "__Female", group: 1 },
    { nodeName: "__Male", group: 3 }
    // { nodeName: "__Other", group: 4 }
  ],
  // links has (nodes-1) links
  links: [
    // ASIAN
    { source: 0, target: 6, value: 1, colorgroup: 1 },
    { source: 0, target: 7, value: 1, colorgroup: 3 },
    // WHITE
    { source: 1, target: 6, value: 7, colorgroup: 1 },
    { source: 1, target: 7, value: 30, colorgroup: 3 },
    // { source: 1, target: 8, value: 1 },
    // BLACK
    { source: 2, target: 6, value: 9, colorgroup: 1 },
    { source: 2, target: 7, value: 5, colorgroup: 3 },
    // HISPANIC
    { source: 3, target: 6, value: 7, colorgroup: 1 },
    { source: 3, target: 7, value: 15, colorgroup: 3 },
    // INDIAN
    { source: 4, target: 6, value: 1, colorgroup: 1 },
    { source: 4, target: 7, value: 1, colorgroup: 3 },
    // OTHER
    { source: 5, target: 6, value: 9, colorgroup: 1 },
    { source: 5, target: 7, value: 1, colorgroup: 3 }
    // { source: 5, target: 8, value: 1 }
  ]
};

var louisiana = {
  nodes: [
    // ARKANSAS
    { nodeName: "ASIAN", group: 2 },
    { nodeName: "WHITE", group: 2 },
    { nodeName: "BLACK", group: 2 },
    { nodeName: "HISPANIC", group: 2 },
    { nodeName: "OTHER", group: 2 },

    { nodeName: "__Female", group: 1 },
    { nodeName: "__Male", group: 3 }
  ],
  // links has (nodes-1) links
  links: [
    // ASIAN
    { source: 0, target: 5, value: 1 },
    { source: 0, target: 6, value: 1 },
    // WHITE
    { source: 1, target: 5, value: 6 },
    { source: 1, target: 6, value: 13 },
    // BLACK
    { source: 2, target: 5, value: 7 },
    { source: 2, target: 6, value: 50 },
    // HISPANIC
    { source: 3, target: 5, value: 1 },
    { source: 3, target: 6, value: 3 },
    // OTHER
    { source: 4, target: 5, value: 1 },
    { source: 4, target: 6, value: 10 }
  ]
};

var newyork = {
  nodes: [
    // ARKANSAS
    { nodeName: "ASIAN", group: 2 },
    { nodeName: "WHITE", group: 2 },
    { nodeName: "BLACK", group: 2 },
    { nodeName: "INDIAN", group: 2 },
    { nodeName: "OTHER", group: 2 },

    { nodeName: "__Female", group: 1 },
    { nodeName: "__Male", group: 3 }
  ],
  // links has (nodes-1) links
  links: [
    // ASIAN
    { source: 0, target: 5, value: 1 },
    { source: 0, target: 6, value: 2 },
    // WHITE
    { source: 1, target: 5, value: 1 },
    { source: 1, target: 6, value: 10 },
    // BLACK
    { source: 2, target: 5, value: 3 },
    { source: 2, target: 6, value: 50 },
    // INDIAN
    { source: 3, target: 5, value: 1 },
    { source: 3, target: 6, value: 1 },
    // other
    { source: 4, target: 5, value: 1 },
    { source: 4, target: 6, value: 25 }
  ]
};
