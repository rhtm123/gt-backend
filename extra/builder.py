def determine_key(class_name):
    class_name = class_name.strip()
    parts = class_name.split('-')

    # Handle special cases first
    special_cases = {
        "text-left": "text-align",
        "text-center": "text-align",
        "text-right": "text-align",
        "text-justify": "text-align",
        "p-auto": "padding-auto",
        "m-auto": "margin-auto",
        "block": "display",
        "inline-block": "display",
        "inline": "display",
        "flex": "display",
        "inline-flex": "display",
        "grid": "display",
        "inline-grid": "display",
        "table": "display",
        "inline-table": "display",
        "table-row": "display",
        "table-cell": "display",
        "hidden": "display"
    }

    if class_name in special_cases:
        return special_cases[class_name]

    # Handle font size cases (text-xs, text-sm, etc.)
    font_size_classes = {
        "text-xs": "font-size",
        "text-sm": "font-size",
        "text-base": "font-size",
        "text-lg": "font-size",
        "text-xl": "font-size",
        "text-2xl": "font-size",
        "text-3xl": "font-size",
        "text-4xl": "font-size",
        "text-5xl": "font-size",
        "text-6xl": "font-size",    
        "text-7xl": "font-size",
        "text-8xl": "font-size",
        "text-9xl": "font-size",
    }

    if class_name in font_size_classes:
        return font_size_classes[class_name]

    # General prefix to CSS property mapping
    prefix_map = {
        "text": "color",
        "bg": "background-color",
        "border": "border-width",  # Default case for border
        "font": "font-weight",
        "w": "width",
        "h": "height",
        "min-w": "min-width",
        "min-h": "min-height",
        "max-w": "max-width",
        "max-h": "max-height",
        "rounded": "border-radius",
        "shadow": "box-shadow",
        "overflow": "overflow",
        "z": "z-index",
        "flex": "flexbox",
        "grid": "grid",
        "justify": "justify-content",
        "items": "align-items",
        "content": "align-content",
        "self": "align-self",
        "place-content": "place-content",
        "place-items": "place-items",
        "place-self": "place-self",
        "inset": "inset",
        "top": "top",
        "bottom": "bottom",
        "left": "left",
        "right": "right",
        "opacity": "opacity",
        "cursor": "cursor",
        "transition": "transition",
        "transform": "transform",
        "scale": "scale",
        "rotate": "rotate",
        "translate": "translate",
        "skew": "skew",
        "origin": "origin",
        "grid-cols": "grid-cols",
        "grid-rows": "grid-rows",
        "col-span": "col-span",
        "row-span": "row-span",
        "gap": "gap",
        "order": "order",
        "p": "padding",
        "pt": "padding-top",
        "pb": "padding-bottom",
        "pl": "padding-left",
        "pr": "padding-right",
        "m": "margin",
        "mt": "margin-top",
        "mb": "margin-bottom",
        "ml": "margin-left",
        "mr": "margin-right",
        "space-x": "space-x",
        "space-y": "space-y",
        "leading": "line-height",
        "tracking": "letter-spacing",
        "list": "list-style",
        "object": "object",
        "outline": "outline",
        "ring": "ring-color",
        "ring-opacity": "ring-opacity",
        "ring-offset": "ring-offset",
        "ring-offset-color": "ring-offset-color",
        "divide-x": "divide-x",
        "divide-y": "divide-y",
        "divide-opacity": "divide-opacity",
        "divide-color": "divide-color",
        "blur": "blur",
        "backdrop": "backdrop",
        "animate": "animation"
    }

    # Handle border color and border style specifically
    if parts[0] == "border":
        if len(parts) == 2:  # Case like "border-solid" or "border-red-500"
            if parts[1] in ["solid", "dashed", "dotted", "double"]:  # Border style
                return "border-style"
            if len(parts) == 3 and parts[1].isdigit():  # Border width
                return "border-width"
            else:  # Assuming it's a color class
                return "border-color"
        elif len(parts) == 3 and parts[1] in {"t", "r", "b", "l"}:  # Case like "border-t-red"
            return f"border-{parts[1]}-width"
        elif len(parts) == 3:  # Handle "border-red" border color shorthand
            return "border-color"

    # Handle color-related classes like "bg-red-500" or "text-blue-600"
    if len(parts) == 3 and parts[0] in {"bg", "text", "border", "ring", "divide"}:
        if not parts[1].isdigit():  # Check if the second part is not a number to differentiate from sizes
            return f"{prefix_map[parts[0]]}"

    # Handle general cases using "".join(parts[:-1])
    prefix = "-".join(parts[:-1])
    if prefix in prefix_map:
        return prefix_map[prefix]

    # Fallback: if no match is found, return the class name
    return class_name


# Examples
# print(determine_key("border-red-200"))
# print(determine_key("ml-2"))  # Output: marginLeft
# print(determine_key("flex"))  # Output: display
# print(determine_key("text-xs"))  # Output: background-color
# # print(determine_key("rounded-lg"))  # Output: border-radius
# # print(determine_key("w-full"))  # Output: width
# print(determine_key("space-x-4"))  # Output: space-x
# print(determine_key("border-t-4")) 

# print(determine_key("border-t-2"))


'''
text-align: text-left, text-center, text-right, text-justify
font-size: text-xs, text-sm, text-base, text-lg, text-xl, text-2xl, text-3xl, text-4xl, text-5xl, text-6xl, text-7xl, text-8xl, text-9xl
font-weight: font-thin, font-extralight, font-light, font-normal, font-medium, font-semibold, font-bold, font-extrabold, font-black
text-color: text-red-500, text-green-500, text-blue-500, ... (all color variants in Tailwind CSS)
border-width: border, border-0, border-2, border-4, border-8
borderTop-width: border-t, border-t-0, border-t-2, border-t-4, border-t-8
borderRight-width: border-r, border-r-0, border-r-2, border-r-4, border-r-8
borderBottom-width: border-b, border-b-0, border-b-2, border-b-4, border-b-8
borderLeft-width: border-l, border-l-0, border-l-2, border-l-4, border-l-8
border-color: border-red-500, border-green-500, border-blue-500, ...
border-style: border-solid, border-dashed, border-dotted, border-double
background-color: bg-red-500, bg-green-500, bg-blue-500, ...
padding: p-0, p-1, p-2, p-3, p-4, p-5, p-6, p-7, p-8, p-9, p-10, p-auto
paddingTop: pt-0, pt-1, pt-2, pt-3, pt-4, pt-5, pt-6, pt-7, pt-8, pt-9, pt-10
paddingBottom: pb-0, pb-1, pb-2, pb-3, pb-4, pb-5, pb-6, pb-7, pb-8, pb-9, pb-10
paddingLeft: pl-0, pl-1, pl-2, pl-3, pl-4, pl-5, pl-6, pl-7, pl-8, pl-9, pl-10
paddingRight: pr-0, pr-1, pr-2, pr-3, pr-4, pr-5, pr-6, pr-7, pr-8, pr-9, pr-10
margin: m-0, m-1, m-2, m-3, m-4, m-5, m-6, m-7, m-8, m-9, m-10, m-auto
marginTop: mt-0, mt-1, mt-2, mt-3, mt-4, mt-5, mt-6, mt-7, mt-8, mt-9, mt-10
marginBottom: mb-0, mb-1, mb-2, mb-3, mb-4, mb-5, mb-6, mb-7, mb-8, mb-9, mb-10
marginLeft: ml-0, ml-1, ml-2, ml-3, ml-4, ml-5, ml-6, ml-7, ml-8, ml-9, ml-10
marginRight: mr-0, mr-1, mr-2, mr-3, mr-4, mr-5, mr-6, mr-7, mr-8, mr-9, mr-10
width: w-0, w-full, w-auto, w-1/2, w-1/3, w-2/3, w-1/4, w-3/4, w-1/5, w-4/5, ...
height: h-0, h-full, h-auto, h-screen, h-1/2, h-1/3, h-2/3, h-1/4, h-3/4, ...
minWidth: min-w-0, min-w-full, min-w-screen, min-w-min, min-w-max
minHeight: min-h-0, min-h-full, min-h-screen, min-h-min, min-h-max
maxWidth: max-w-xs, max-w-sm, max-w-md, max-w-lg, max-w-xl, max-w-2xl, ...
maxHeight: max-h-0, max-h-full, max-h-screen
border-radius: rounded-none, rounded-sm, rounded, rounded-md, rounded-lg, rounded-xl, rounded-2xl, rounded-3xl, rounded-full
box-shadow: shadow-sm, shadow, shadow-md, shadow-lg, shadow-xl, shadow-2xl, shadow-inner, shadow-outline, shadow-none
overflow: overflow-auto, overflow-hidden, overflow-visible, overflow-scroll
z-index: z-0, z-10, z-20, z-30, z-40, z-50, z-auto
gap: gap-0, gap-1, gap-2, gap-3, gap-4, gap-5, gap-6, gap-7, gap-8, gap-9, gap-10
display: block, inline-block, inline, flex, inline-flex, grid, inline-grid, table, inline-table, table-row, table-cell, hidden
justify-content: justify-start, justify-end, justify-center, justify-between, justify-around, justify-evenly
align-items: items-start, items-end, items-center, items-baseline, items-stretch
align-content: content-start, content-end, content-center, content-between, content-around, content-evenly
align-self: self-auto, self-start, self-end, self-center, self-stretch
place-content: place-content-start, place-content-end, place-content-center, place-content-between, place-content-around, place-content-evenly, place-content-stretch
place-items: place-items-start, place-items-end, place-items-center, place-items-stretch
place-self: place-self-auto, place-self-start, place-self-end, place-self-center, place-self-stretch
inset: inset-0, inset-y-0, inset-x-0, inset-px, inset-full, inset-1/2, ...
top: top-0, top-1, top-2, top-3, top-4, top-5, top-6, top-7, top-8, top-9, top-10
bottom: bottom-0, bottom-1, bottom-2, bottom-3, bottom-4, bottom-5, bottom-6, bottom-7, bottom-8, bottom-9, bottom-10
left: left-0, left-1, left-2, left-3, left-4, left-5, left-6, left-7, left-8, left-9, left-10
right: right-0, right-1, right-2, right-3, right-4, right-5, right-6, right-7, right-8, right-9, right-10
opacity: opacity-0, opacity-25, opacity-50, opacity-75, opacity-100
cursor: cursor-auto, cursor-default, cursor-pointer, cursor-wait, cursor-text, cursor-move, cursor-not-allowed, cursor-none
transition: transition-none, transition-all, transition, transition-colors, transition-opacity, transition-shadow, transition-transform
transform: transform, transform-none
scale: scale-0, scale-50, scale-75, scale-90, scale-95, scale-100, scale-105, scale-110, scale-125, scale-150
rotate: rotate-0, rotate-45, rotate-90, rotate-180, -rotate-45, -rotate-90, -rotate-180
translate: translate-x-0, translate-x-1, translate-x-2, translate-x-3, translate-y-0, translate-y-1, translate-y-2, translate-y-3, -translate-x-1, -translate-y-1, ...
skew: skew-x-0, skew-x-3, skew-y-0, skew-y-3, -skew-x-3, -skew-y-3
origin: origin-center, origin-top, origin-top-right, origin-right, origin-bottom-right, origin-bottom, origin-bottom-left, origin-left, origin-top-left
grid-template-columns: grid-cols-1, grid-cols-2, grid-cols-3, grid-cols-4, grid-cols-5, grid-cols-6, grid-cols-7, grid-cols-8, grid-cols-9, grid-cols-10, grid-cols-11, grid-cols-12
grid-template-rows: grid-rows-1, grid-rows-2, grid-rows-3, grid-rows-4, grid-rows-5, grid-rows-6
grid-column: col-auto, col-span-1, col-span-2, col-span-3, col-span-4, col-span-5, col-span-6, col-span-7, col-span-8, col-span-9, col-span-10, col-span-11, col-span-12
grid-row: row-auto, row-span-1, row-span-2, row-span-3, row-span-4, row-span-5, row-span-6
gap: gap-0, gap-1, gap-2, gap-3, gap-4, gap-5, gap-6, gap-7, gap-8, gap-9, gap-10
flex: flex-row, flex-row-reverse, flex-col, flex-col-reverse, flex-wrap, flex-wrap-reverse, flex-no-wrap, flex-1, flex-auto, flex-initial, flex-none
order: order-first, order-last, order-none, order-1, order-2, order-3, order-4, order-5, order-6, order-7, order-8, order-9, order-10, order-11, order-12
'''