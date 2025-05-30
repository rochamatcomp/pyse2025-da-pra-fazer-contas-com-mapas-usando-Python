
areas = response.xpath('//map/area')

header = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">'
footer = '</svg>'

polygons = list(get_polygon(areas))

def get_polygon(areas):
    for area in areas:
        polygon_id = area.xpath("./@id").get()
        points = area.xpath("@coords").get()
        title = area.xpath("./@title").get()
        name = area.xpath("./@data-nome").get()
        number = area.xpath("./@data-numero").get()
        phone = area.xpath("./@data-telefone").get()
        email = area.xpath("./@data-email").get()
        site = area.xpath("./@data-site").get()
        description = area.xpath("./@data-descricao").get().replace('\n', '')
        store = area.xpath("./@data-loja").get()
        current = area.xpath("./@data-current").get()

        polygon = (
            f"<polygon"
            f" {points=}"
            f" {title=}"
            f" {name=}"
            f" {number=}"
            f" {phone=}"
            f" {email=}"
            f" {site=}"
            f" {description=}"
            f" {store=}"
            f" {current=}"
            f' fill="#FFADAD"'
            f' stroke="black"'
            f' stroke-width="1"'
            f' id="{polygon_id}"'
            f' />'
        )

        yield polygon
