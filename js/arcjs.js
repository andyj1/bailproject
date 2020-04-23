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
    { source: 0, target: 6, value: 1 },
    { source: 0, target: 7, value: 1 },
    // WHITE
    { source: 1, target: 6, value: 7 },
    { source: 1, target: 7, value: 25 },
    // { source: 1, target: 8, value: 1 },
    // BLACK
    { source: 2, target: 6, value: 2 },
    { source: 2, target: 7, value: 7 },
    // HISPANIC
    { source: 3, target: 6, value: 2 },
    { source: 3, target: 7, value: 5 },
    // INDIAN
    { source: 4, target: 6, value: 1 },
    { source: 4, target: 7, value: 1 },
    // OTHER
    { source: 5, target: 6, value: 1 },
    { source: 5, target: 7, value: 2 }
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
    { source: 1, target: 5, value: 3 },
    { source: 1, target: 6, value: 7 },
    // BLACK
    { source: 2, target: 5, value: 5 },
    { source: 2, target: 6, value: 32 },
    // HISPANIC
    { source: 3, target: 5, value: 1 },
    { source: 3, target: 6, value: 2 },
    // OTHER
    { source: 4, target: 5, value: 1 },
    { source: 4, target: 6, value: 1 }
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
    { source: 0, target: 6, value: 1 },
    // WHITE
    { source: 1, target: 5, value: 1 },
    { source: 1, target: 6, value: 5 },
    // BLACK
    { source: 2, target: 5, value: 2 },
    { source: 2, target: 6, value: 24 },
    // INDIAN
    { source: 3, target: 5, value: 1 },
    { source: 3, target: 6, value: 2 },
    // other
    { source: 4, target: 5, value: 1 },
    { source: 4, target: 6, value: 11 }
  ]
};
