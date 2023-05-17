import tinify
tinify.key = "5cKR0fbQkxBccF570LNqKKFjd413MKmM"

source = tinify.from_file("./API_Imagem/img/martim-pescador.jpg")

source.to_file("./API_Imagem/img/martim-pescador_otimizada.jpg")

resized = source.resize(
    method="fit",
    width=200,
    height=200
)
resized.to_file("./API_Imagem/img/martim-pescador_200px.jpg")

converted = source.convert(type=["image/webp","image/png"])

extension = converted.result().extension

converted.to_file(f"./API_Imagem/img/martim-pescador_convertida.{extension}")