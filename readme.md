<!-- # :page_with_curl: Chinese Live-Streaming E-Commerce Morph Resolution: Datasets and Methods
<p align="center">
    <a href="https://github.com/OpenBMB/AgentVerse/blob/main/LICENSE">
        <img alt="License: Apache2" src="https://img.shields.io/badge/License-Apache_2.0-green.svg">
    </a>
    <a href="https://www.python.org/downloads/release/python-3916/">
        <img alt="Python Version" src="https://img.shields.io/badge/python-3.9+-blue.svg">
    </a>
    <a href="https://github.com/OpenBMB/AgentVerse/actions/">
        <img alt="Build" src="https://img.shields.io/github/actions/workflow/status/OpenBMB/AgentVerse/test.yml">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-black">

      <a href="https://huggingface.co/AgentVerse">
        <img alt="HuggingFace" src="https://img.shields.io/badge/hugging_face-play-yellow">
    </a>
    <a href="https://discord.gg/gDAXfjMw">
        <img alt="Discord" src="https://img.shields.io/badge/AgentVerse-Discord-purple?style=flat">
    </a>


</p> -->
<!-- ---
## Data Annotate Website 💻

The annotation website we use consists of a front-end (Vue) and a back-end (Flask), which can be found at labelwebsite.
We provide a short video to demonstrate the specific annotation process.
Please note that the annotators have already been trained. -->

<h1 align="center"> 📣 Chinese Live-Streaming E-Commerce Morph Resolution: Datasets and Methods</h1>

<p align="center">
    <a href="https://github.com/OpenBMB/AgentVerse/blob/main/LICENSE">
        <img alt="License: Apache2" src="https://img.shields.io/badge/License-Apache_2.0-green.svg">
    </a>
    <a href="https://www.python.org/downloads/release/python-3916/">
        <img alt="Python Version" src="https://img.shields.io/badge/python-3.9+-blue.svg">
    </a>
    <a href="https://github.com/OpenBMB/AgentVerse/actions/">
        <img alt="Build" src="https://img.shields.io/github/actions/workflow/status/OpenBMB/AgentVerse/test.yml">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-black">    
</p>

<!-- <p align="center">
<img src="./assets/example.png" width="512">
</p> -->

---

**This is repository for the Chinese Live-Streaming E-Commerce Morph Resolution: Datasets and Methods.**

<p align="center">
<img src="./assets/example.png" width="512">
</p>

---

# 📰 What's New

- [2025/8/3] 🚀 We reannotate health AMR and extend AMR dataset to general domain. Proposed JointMER and CDRF, two state-of-the-art morph resolution methods!

- [2025/3/1] 🚀 [Chinese Morph Resolution in E-commerce Live Streaming Scenarios](https://aclanthology.org/2025.naacl-industry.32.pdf) was accepted by NAACL Industry Track!

# Contents

- [📰 What's New](#-whats-new)
- [Contents](#contents)
- [🚀 Getting Started](#-getting-started)
  - [Annotation Website](#webiste)
  - [Health and General AMR](#environment-variables)
  - [Methods](#simulation)
    - [environment prepare](#framework-required-modules)
    - [model checkpoint](#cli-example)
    - [suage](#gui-example)
- [Contact](#contact)

## 💻Data Annotate Website

The annotation website we use consists of a front-end (Vue) and a back-end (Flask), which can be found at **labelwebsite**. We provide a short video to demonstrate the specific annotation process.
**Please note that the annotators have already been trained.**

<div align="center">

[![Watch the video](https://img.youtube.com/vi/OBbo5ZwJBlk/hqdefault.jpg)](https://www.youtube.com/watch?v=OBbo5ZwJBlk)

</div>

<!-- [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/aJpaQB-ylks/0.jpg)](https://youtu.be/R_epYJPtquU) -->

## 🗄 Health AMR and General AMR

The dataset include health and general amr, which can be found at **dataset**.

## ✨ Methods

The dataset include health and general amr, which can be found at **dataset**.

## Environment Variables

You need to export your OpenAI API key as follows：

```bash
# Export your OpenAI API key
export OPENAI_API_KEY="your_api_key_here"
```

If you want use Azure OpenAI services, please export your Azure OpenAI key and OpenAI API base as follows：

```bash
export AZURE_OPENAI_API_KEY="your_api_key_here"
export AZURE_OPENAI_API_BASE="your_api_base_here"
```

# Contact

Project Creation: zjh2001@qq.com
