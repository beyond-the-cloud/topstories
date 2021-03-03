# topstories
Get the top 500 stories through [Hacker News API](https://github.com/HackerNews/API#new-top-and-best-stories)

```bash
docker build -t topstories:1.0 .

docker run -it topstories:1.0

docker tag topstories:1.0 bh7cw/topstories:1.0
docker push bh7cw/topstories:1.0
```