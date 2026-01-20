---
permalink: /
title: 
layout: null
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<div class="lecun-classic-layout">
<style>
  /* 90년대 클래식 학계 스타일 */
  .lecun-classic-layout {
    font-family: "Times New Roman", Times, serif;
    background-color: #FFFFFF; /* 전체 배경 */
    color: #000000;
    margin: 0;
    padding: 0;
    line-height: 1.45;
    font-size: 17px;
  }

  /* 가로 100% 레이아웃 */
  .lecun-main-table {
    width: 100%;
    border-collapse: collapse;
    border-spacing: 0;
  }

  /* 왼쪽 사이드바: 사진과 메뉴 */
  .lecun-sidebar {
    width: 150px;
    background-color: #f4e8d1; /* 사이드바 배경 */
    border-right: 1px solid #B0C4DE; /* 구분선 */
    padding: 12px 10px;
    vertical-align: top;
  }

  .lecun-sidebar img.profile-pic {
    width: 150px;
    border: none;
    margin-bottom: 16px;
  }

  .lecun-sidebar a {
    display: block;
    color: #0000EE; /* 일반 링크 */
    text-decoration: none;
    font-size: 14px;
    margin-bottom: 6px;
    font-weight: bold;
    letter-spacing: 0.4px;
  }

  .lecun-sidebar .nav-divider {
    height: 6px;
    margin: 12px 0;
    background: linear-gradient(to bottom, #b7c9df 0%, #5c7aa7 50%, #2d3f5c 100%);
    border-top: 1px solid #c9d7ea;
    border-bottom: 1px solid #1a2537;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
  }

  /* 메인 콘텐츠 영역 */
  .lecun-content {
    padding: 35px 55px 70px 3px;
    vertical-align: top;
    font-size: 17px;
  }

  /* 르쿤식 파란색 큰 제목 */
  .lecun-header-name {
    text-align: center;
    margin-bottom: 40px;
  }
  .lecun-header-name h1 {
    font-size: 50px;
    color: #5e77a2;
    font-style: italic;
    margin: 0;
    text-shadow: 1px 1px #cccccc;
  }

  /* 개 촌스러운 회색 섹션 바 */
  .lecun-section-header {
    background-color: #E8E8E8; /* 섹션 바 */
    border-top: 1px solid #333;
    border-bottom: 1px solid #333;
    padding: 5px 15px;
    font-weight: bold;
    font-size: 18px;
    color: #22427C; /* 섹션 제목 글자 */
    margin-top: 35px;
    margin-bottom: 15px;
  }

  /* 뱃지 및 리스트 스타일 유지 */
  .lecun-content p, .lecun-content li {
    font-size: 17px;
    margin-bottom: 14px;
    line-height: 1.55;
  }
  
  .lecun-content a {
    color: #18397A;
    text-decoration: underline;
  }

  .footer-timestamp {
    margin-top: 60px;
    border-top: 1px solid #000;
    font-size: 11px;
    color: #444;
    padding-top: 10px;
  }
</style>

<table class="lecun-main-table">
  <tr>
    <td class="lecun-sidebar">
      <img src="images/myprofile.png" class="profile-pic" alt="Jaeik Kim">
      
      <div class="lecun-nav">
        <a href="#home">HOME</a>
        <a href="#news">NEWS</a>
        <a href="#publications">PUBLICATIONS</a>
        <div class="nav-divider"></div>
        <a href="mailto:jake630@snu.ac.kr">EMAIL</a>
        <a href="https://github.com/KIM-JAKE">GITHUB</a>
        <a href="https://scholar.google.com/citations?user=fwpoQpQAAAAJ&hl=ko">GOOGLE SCHOLAR</a>
        <a href="https://www.linkedin.com/in/jaeik-kim-571200282/">LINKEDIN</a>
        <div class="nav-divider"></div>
        <!-- <img src="https://yann.lecun.com/ex/images/nips_logo.gif" width="80" style="margin-top:10px;"> -->
        <!-- <img src="https://yann.lecun.com/ex/images/djvu_logo.gif" width="80" style="margin-top:5px;"> -->
      </div>
    </td>

    <td class="lecun-content">
      <div class="lecun-header-name">
        <h1>Jaeik Kim</h1>
      </div>

      <div id="home">
        <p>
          I am a first-year M.S. student in the <a href="https://aidas.snu.ac.kr/">AIDAS Lab</a> at Seoul National University, advised by Jaeyoung Do. <br>
          My research focuses on <b>model editing and personalization</b>, <b>diffusion-based language models</b>, and <b>omni-modal models</b>.
        </p>
      </div>

      <div class="lecun-section-header" id="news">News</div>
      <p>
        <strong>2025</strong><br>
        🔥 Two of our papers have been accepted to the <b>39th Annual Conference on Neural Information Processing Systems (NeurIPS 2025)</b> <br>
        🔥 Our paper has been accepted to the <b>2025 International Conference on Machine Learning (ICML)</b>
      </p>

      <div class="lecun-section-header" id="publications">Publications</div>
      
      <p>
        <img src="https://img.shields.io/badge/NeurIPS-2025-CC0000" alt="NeurIPS"> 
        <strong><a href="https://arxiv.org/abs/2509.22820">MMPB: It’s Time for Multi-Modal Personalization</a></strong><br>
        <u>Jaeik Kim</u>, Woojin Kim, Woohyeon Park, Jaeyoung Do<br>
        <i>In Conference on Neural Information Processing Systems (NeurIPS), 2025</i>
      </p>

      <hr color="#eee">

      <p>
        <img src="https://img.shields.io/badge/NeurIPS-2025-CC0000" alt="NeurIPS"> 
        <strong><a href="https://arxiv.org/abs/2510.11268v1">Exploring and Leveraging Class Vectors for Classifier Editing</a></strong><br>
        <u>Jaeik Kim</u>, Jaeyoung Do<br>
        <i>In Conference on Neural Information Processing Systems (NeurIPS), 2025</i>
      </p>

      <hr color="#eee">

      <p>
        <img src="https://img.shields.io/badge/ICML-2025-007ACC" alt="ICML"> 
        <strong><a href="https://arxiv.org/abs/2506.08391">SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding</a></strong><br>
        Woohyeon Park, Woojin Kim, <u>Jaeik Kim</u>, Jaeyoung Do<br>
        <i>In International Conference on Machine Learning (ICML), 2025</i>
      </p>

      <div class="lecun-section-header" id="social">Professional Links</div>
      <p>
        <strong>Email</strong>: <a href="mailto:jake630@snu.ac.kr">jake630@snu.ac.kr</a><br>
        <strong>Google Scholar</strong>: <a href="https://scholar.google.com/citations?user=fwpoQpQAAAAJ&hl=ko">scholar.google.com/citations?user=fwpoQpQAAAAJ</a><br>
        <strong>GitHub</strong>: <a href="https://github.com/KIM-JAKE">github.com/KIM-JAKE</a><br>
        <strong>LinkedIn</strong>: <a href="https://www.linkedin.com/in/jaeik-kim-571200282/">linkedin.com/in/jaeik-kim-571200282</a>
      </p>


      <div class="footer-timestamp">
        Last updated: January 2026
      </div>
    </td>
  </tr>
</table>
</div>
