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
      <div class="module_box" style="height:60vh;">
        <!-- 左边内容 -->
        <div style="flex: 0 1 25%;">
          <div style="width:100%; height:50%;"  >
            <dv-border-box-13>
                <div id="Picture1" style="width:100%;height:109%;top:25px;right:7px;">

                </div>
            </dv-border-box-13>
          </div>
          <div style="width:100%; height:50%;" >
            <dv-border-box-8>
              <div id="Picture2" style="width:100%;height:100%;">

              </div>
            </dv-border-box-8>
          </div>
        </div>
        <!-- 中间内容 -->
        <div style="flex: 0 1 50%;">
          <div style="width:100%; height:100%;">
              <div style="display: flex;width: 100%; height: 100%;">
                <dv-border-box-6 :color="['blue','green']">
                  <div id="Picture4" style="width:97%;height:96%;border:1px solid black;">
                  
                  </div>
                </dv-border-box-6>
              </div>
          </div>
        </div>
        <!-- 右边内容 -->
        <div style="flex: 0 1 25%;">
          <div style="width:100%; height:50%;">
              <dv-border-box-13>
                <div id="Picture7" style="width:100%;height:100%;">

                </div>
              </dv-border-box-13>
          </div>
          <div style="width:100%; height:50%;">
              <dv-border-box-8 :reverse="true">
                <div id="Picture8" style="width:100%;height:115%;">

                </div>
              </dv-border-box-8>
          </div>
        </div>
      </div>
      
      <!-------------------------- 底下内容 --------------------------->
      <div class="module_box" style="height:33vh; border: 1px solid black">
        <div style="flex: 0 1 30%;">
          <dv-border-box-9>
            <div id="Picture5" style="width:91.1%;height:86%;">

            </div>
          </dv-border-box-9>
        </div>
        <div style="flex: 0 1 40%;">
          <dv-border-box-10>
            <div id="Picture3" style="width:95%;height:100%;">

            </div>
          </dv-border-box-10>
        </div>
        <div style="flex: 0 1 30%;">
          <dv-border-box-12>
            <div id="Picture6" style="width:91.1%;height:86%;">

            </div>
          </dv-border-box-12>
        </div>
      </div>
    </dv-full-screen-container>
    <!-- 全屏容器 -->
  </div>
  <!-- 整个视窗 -->
</template>



<script>
import axios from 'axios';
import * as echarts from 'echarts';
import chinaJson from '@/assets/json/china.json';

export default {
data:function(){
      return {

      }
  },
  mounted:function(){
      echarts.registerMap('china',chinaJson);
        this.get_picture4();
  },
  methods:{
    get_picture4(){
          axios.get("http://127.0.0.1:12345/picture4").then(
            response =>{
              var data = response.data;
              // console.log(data);
              var province = data.name;
              var value = data.value;
              console.log(province);
              console.log(value);
              var province_data = [];
              for(var i=0;i<province.length;i++){
                  province_data.push({value:value[i],name:province[i]});
              }
              var myChart = echarts.init(document.getElementById("Picture4"));
              var option = get_picture4_option(province_data);
              myChart.setOption(option);
            }
          )
        },
  }
}



// 图4：物联网行业企业全国分布（地图）
function get_picture4_option(province_data){
  var option = {
    title:{
      text:'物联网行业全国分布',
      textStyle:{
        color:'#FEFEFE',
        fontSize:25,
      }
    },
    tooltip:{
      trigger: 'item',
    },
    legend:{
      orient:'horizontal',
      textStyle:{color:'#fff'},
      x:'left',
      y:'20',
      data:['物联网行业地域分布']
    },
    visualMap:{
      textStyle:{color:'#fff'},
      x:'left',
      y:'bottom',
      splitList:[
        {start:370},
        {start:320,end:370},
        {start:270,end:320},  
        {start:220,end:270},
        {start:170,end:220},
        {start:120,end:170},
        {start:70,end:120},
        {start:50,end:70},
        {start:40,end:50},
        {start:30,end:40},
        {start:20,end:30},
        {start:10,end:20},
        {start:5,end:10},
        {start:2,end:5},
        {start:0,end:2}
      ],
      color: ['#de1c31','#FF0000','#FF4500','#FFA500','#f1ca17',
        '#f8df72','#2775b6','#2177b8','#abd9e9'],
    },
    series:[
      {
        name:'全国分布',
        type:'map',
        map: 'china',
        center:[104.114129, 35.550339],
        zoom: 1.75,
        roam: true,
        itemStyle:{
          normal:{
            label:{show:true,textStyle:{color:"rgb(249, 249, 249)"}}
          }
        },
        emphasis:{
          label:{show:true},
        },
        data:province_data
      }
    ]
  }
  return option;
}

</script>