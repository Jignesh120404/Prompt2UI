figma.showUI(__html__, {
  width: 300,
  height: 500,
});

// let designData;
let image_list: Array<string> = [];
figma.ui.onmessage = (msg) => {
  //   console.log(msg.type, msg.data);
  if (msg.type === "generate") {
    image_list = msg.data.image_list;
    createDesign(msg.data.data);
    console.log(image_list);
  }
};

// const frame = figma.createFrame();

// frame.name = "Frame";
console.log("image_links", image_list);

async function createDesign(data: any[]) {
  let idx = 0;
  for (const element of data) {
    let figmaNode: SceneNode;
    if (element.type === "RECTANGLE") {
      figmaNode = figma.createRectangle();
      figmaNode.x = element.x;
      figmaNode.y = element.y;
      figmaNode.resize(element.width, element.height);
      figmaNode.name = element.name;
      figmaNode.setPluginData("customNodeId", element.id);
      figmaNode.fills = element.fills;
      figmaNode.cornerRadius = element.cornerRadius;
      if (element.name === "IMAGENODE") {
        console.log("setting background image ", idx, image_list[idx]);
        figma
          .createImageAsync(image_list[idx])
          .then(async (image: Image) => {
            // Render the image by filling the rectangle.
            if ("fills" in figmaNode) {
              figmaNode.fills = [
                {
                  type: "IMAGE",
                  imageHash: image.hash,
                  scaleMode: "FILL",
                },
              ];

              console.log("background image setted ", idx);
            }
          })
          .catch((err) => {
            console.log("ERROR setting bg image", err);
          });
        idx++;
      } else if (element.name.includes("Image")) {
        console.log("setting image ", idx, image_list[idx]);
        figma
          .createImageAsync(image_list[idx])
          .then(async (image: Image) => {
            // Render the image by filling the rectangle.
            if ("fills" in figmaNode) {
              figmaNode.fills = [
                {
                  type: "IMAGE",
                  imageHash: image.hash,
                  scaleMode: "FILL",
                },
              ];

              console.log("image setted ", idx);
            }
          })
          .catch((err) => {
            console.log(err);
          });
        idx++;
      }
      //   frame.appendChild(figmaNode);
    } else if (element.type === "TEXT") {
      await figma.loadFontAsync(element.fontName);
      figmaNode = figma.createText();
      figmaNode.x = element.x;
      figmaNode.y = element.y;
      figmaNode.resize(element.width, element.height);
      figmaNode.characters = element.characters;
      figmaNode.fontSize = element.fontSize;
      figmaNode.name = element.name;
      figmaNode.fontName = element.fontName;
      figmaNode.fills = element.fills;
      figmaNode.textAlignHorizontal = element.textAlignHorizontal;
      figmaNode.textAlignVertical = element.textAlignVertical;
      figmaNode.setPluginData("customNodeId", element.id);
      //   frame.appendChild(figmaNode);
    } else if (element.type === "LINE") {
      figmaNode = figma.createLine();
      figmaNode.x = element.x;
      figmaNode.y = element.y;
      figmaNode.resize(element.width, element.height);
      figmaNode.fills = element.fills;
      figmaNode.name = element.name;
      figmaNode.setPluginData("customNodeId", element.id);
      //   frame.appendChild(figmaNode);
    }
  }
  //   figma.viewport.scrollAndZoomIntoView(frame.children);
  //   figma.group([frame], figma.currentPage);
  //   const minX = Math.min(...data.map((node) => node.x));
  //   const minY = Math.min(...data.map((node) => node.y));
  //   const maxX = Math.max(...data.map((node) => node.x + node.width));
  //   const maxY = Math.max(...data.map((node) => node.y + node.height));
  //   frame.resize(maxX - minX, maxY - minY);
  //   frame.x = minX;
  //   frame.y = minY;
}
// createDesign(data);
// console.log("--mydata--", data);
