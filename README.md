# Palette
The unique feature of this project is the color-based sorting of logos into a spectrum, presented in two formats: **grid** and **dense paving**. 

## *UniLogo*: assembles the logos of the top 1000 universities according to the *Academic Ranking of World Universities* (ARWU).
### Dense paving
Below is the densely paved logos for **835** universities:
<figure>
<img src="outputs/Dense-1000-logos.png" alt="Densely paved logos" style="width:95%" />
</figure>

### Grid
Below is logos in **32*32** grid, if universities share same coordinate, only the university with the best rank is shown.
<figure>
<img src="outputs/Grid 32 by 32.png" alt="Logos in grid" style="width:95%" />
</figure>

## *Passports*: assembles the images of passports crawled from WikiPedia
### Dense paving
Below is the densely paved logos for **199** passports:
<figure>
<img src="outputs/Dense-200-logos.png" alt="Densely paved logos" style="width:95%" />
</figure>

### Grid
Below is logos in **15*15** grid, if passports share same coordinate, sorted by the first letter of countries' codes ([ISO 3166-1 Alpha‑2](https://en.wikipedia.org/wiki/ISO_3166-1))
<figure>
<img src="outputs/Grid 15 by 15.png" alt="Logos in grid" style="width:95%" />
</figure>

## Next Steps

- [ ] Consider the proportion of the dominant color in the logo during sorting.
- [ ] Geometric clustering


## Acknowledgements
The project is inspired by the report from Southern Metropolis Daily: [We also statisticized the emblems of 920 colleges and universities and found that some emblems were drawn by Word (我们又统计了920所高校的校徽，发现有学校是用word画的)](https://mp.weixin.qq.com/s?search_click_id=10444709157102856276-1687166234989-9867360616&__biz=MTk1MjIwODAwMQ==&mid=207756532&idx=2&sn=beb910454354085923a5a5923d1a70cd&chksm=d5f51f1ae282960cbff6019f1bd868acd33ce9057724ca93f80621750732ea48ea347a1ab6cc&scene=7&subscene=10000&clicktime=1687166235&enterid=1687166235&sessionid=0&ascene=65&fasttmpl_type=0&fasttmpl_fullversion=6730971-en_US-zip&fasttmpl_flag=0&realreporttime=1687166235014#rd)

Thanks to [ARWU](https://www.shanghairanking.com/rankings/arwu/2022) for the data, and to the respective universities for their logos.

Thanks to [WikiPedia](https://en.wikipedia.org/wiki/List_of_passports) for the passport images.

[Twins repo](https://github.com/zhoudaxia233/UniLogo)

*Note: This project is for research purposes only. All logos are trademarks of their respective universities and are used under the principles of fair use.*
