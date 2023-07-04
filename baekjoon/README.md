# 📃 프로젝트 개요

  <p align="center"><img src="https://github.com/SS-hj/DACON-objectdetection/assets/54202082/b40140a1-62cc-40a3-abd4-74a560de8302" width="100%"/></p>

합성데이터란 실제 환경에서 수집되거나 측정되는 것이 아니라 디지털 환경에서 생성되는 데이터셋으로, 최근 방대한 양질의 데이터셋이 필요해짐에 따라 그 중요성이 대두되고 있습니다.
이러한 합성데이터를 활용하여 자동차 탐지를 수행하여, 34가지의 자동차 세부모델까지 판별하는 AI 모델을 개발하는 대회입니다.

<br/>

# 💾 데이터셋

- 전체 이미지 개수 : 9754장 (Training : 6481장, Test : 1700장)
- 34 class : chevrolet_malibu_sedan_2012_2016, chevrolet_malibu_sedan_2017_2019,..., ssangyong_tivoli_suv_2016_2020
- 이미지 크기 : (1920, 1040)

<br/>

# ✏ 프로젝트 수행 방법

## Data Processing

- StratifiedGroupKFold
- Heavy Augmentation
- Validation Augmentation for Synthetic data

## Modeling

- Model
    - Cascade RCNN
    - Cascade Mask RCNN
- Backbone
  - Swin Transformer - Small
  - ConvNeXt - Tiny
  - Res2Net

<br/>

# 🏆 프로젝트 결과
- Ensemble

  <p align="center"><img src="https://github.com/SS-hj/DACON-objectdetection/assets/54202082/aac2ca29-e941-414e-a6fb-933ca1bdf2cc" alt="trash" width="50%" height="50%" /></p>

- Score

  <p align="center"><img src="https://github.com/SS-hj/DACON-objectdetection/assets/54202082/6969b445-9488-446d-b757-72741ae1ef3f" width="100%" height="100%" /></p>

<br/>


# 팀원 소개


|         [황순영](https://github.com/soonyoung-hwang)         |             [이하정](https://github.com/SS-hj)              |     
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| swin, res2net 모델링, 앙상블 | 데이터 전처리, convnext 모델링 |