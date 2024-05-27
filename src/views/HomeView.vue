<!-- 模板1 -->
<template>
    <!-- 整个视窗 -->
    <div class="content bg">
      <!-- 全屏容器 -->
      <dv-full-screen-container>
  
        <!------------------------------ 标题 ------------------------------>
        <div class="module_box" style="height: 7vh;">
          <div style="flex:0 1 30%;">
            <dv-decoration-3 style="width:100%;height:30px;" />
            <dv-decoration-12 style="width:100%;height:5px;" />
          </div>
          <div style="flex:0 1 40%;">
            <div style="display: flex;width: 100%;">
                <dv-decoration-8 :reverse="true" style="width:300px;height:50px;" />
                <dv-decoration-11 style="width:360px;height:60px; font-size: 32px; font-weight: bold;color:#FEFEFE">物联网行业就业分析</dv-decoration-11>
                <dv-decoration-8 style="width:300px;height:50px;" />
            </div>
          </div>
          <div style="flex:0 1 30%;">
            <dv-decoration-3 style="width:100%;height:30px;" />
            <dv-decoration-12 style="width:100%;height:5px;" />
          </div>
        </div>
  
        <!-------------------------- 中间内容 --------------------------->
        <div class="module_box" style="height:60vh; border: 1px solid black">
          <!-- 左边内容 -->
          <div style="flex: 0 1 25%; border: 1px solid black">
            <div style="width:100%; height:50%; border: 1px solid black">
              <dv-border-box-1>
                左边第一个图
              </dv-border-box-1>
            </div>
            <div style="width:100%; height:50%; border: 1px solid black">
              <dv-border-box-13>
                左边第二个图
              </dv-border-box-13>
            </div>
          </div>
          <!-- 中间内容 -->
          <div style="flex: 0 1 50%; border: 1px solid black">
            <div style="width:100%; height:100%;">
              <dv-border-box-6 :color="['blue','green']">
                中间内容
              </dv-border-box-6>
            </div>
          </div>
          <!-- 右边内容 -->
          <div style="flex: 0 1 25%; border: 1px solid black">
            <div style="width:100%; height:40%; border: 1px solid black">
              <dv-border-box-1>
                右边第一个图
              </dv-border-box-1>
            </div>
            <div style="width:100%; height:60%; border: 1px solid black">
              <dv-border-box-13>
                右边第二个图
              </dv-border-box-13>
            </div>
          </div>
        </div>
        
        <!-------------------------- 底下内容 --------------------------->
        <div class="module_box" style="height:30vh; border: 1px solid black">
          <div style="flex: 0 1 30%; border: 1px solid black">
            <dv-border-box-9>
              左边内容
            </dv-border-box-9>
          </div>
          <div style="flex: 0 1 40%; border: 1px solid black">
            <dv-border-box-10>
              中间内容
            </dv-border-box-10>
          </div>
          <div style="flex: 0 1 30%; border: 1px solid black">
            <dv-border-box-9>
              右边内容
            </dv-border-box-9>
          </div>
        </div>
      </dv-full-screen-container>
      <!-- 全屏容器 -->
    </div>
    <!-- 整个视窗 -->
  </template>