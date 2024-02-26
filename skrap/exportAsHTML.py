
heinn = "Þetta væri svo e-ð annað headline"
texti = "grein um þá allt annað jafnvel hér"
timi = "08.02.24 kl 06:54"

with open("test.html", "a", encoding="utf-8") as f:
    cont = f"""
    <h2>{heinn}</h2>
    <p>{texti}</p>
    <p>{timi}</p>
    """
    f.write(cont)

