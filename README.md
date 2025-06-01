# Zadanie 2 – GitHub Actions: Budowa i Publikacja Obrazu Dockera

## Opis projektu

Aplikacja webowa (zadanie 1) została zmodyfikowana i zapisana w folderze `src`. Projekt umożliwia użytkownikowi wybór kraju i miasta w celu sprawdzenia aktualnej pogody (API: OpenWeatherMap).

## Sekrety użyte w workflow

W zakładce *Settings > Secrets and variables > Actions* utworzono:

- `GHCR_TOKEN` – token PAT z uprawnieniami do `write:packages`
- `DOCKERHUB_USERNAME` – nazwa użytkownika DockerHub (`97819`)
- `DOCKERHUB_TOKEN` – token do DockerHub
- `WEATHER_API_KEY` – klucz API do serwisu OpenWeatherMap

## Jak działa workflow?

Workflow `.github/workflows/docker-build.yml` wykonuje:

1. **checkout** kodu źródłowego
2. **instalację QEMU i Buildx**
3. **logowanie do GitHub Container Registry** i **DockerHub**
4. **budowę obrazu Dockera** dla `linux/amd64` oraz `linux/arm64`
5. **użycie cache** dla przyspieszenia buildów
6. **publikację obrazu** do `ghcr.io/zzo0mmee/pawcho-zad2`
7. **skanowanie podatności CVE** przy pomocy `trivy`

## Potwierdzenie działania GitHub Actions

Chain GHAction został uruchomiony automatycznie i zakończył się sukcesem, co można potwierdzić w zakładce **Actions**:

`Final commit` – zakończony poprawnie  
Link: [https://github.com/zZo0mMeE/pawcho_zad2/actions](https://github.com/zZo0mMeE/pawcho_zad2/actions)