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
import * as echarts from 'echarts';
import axios from 'axios';
import chinaJson from '@/assets/json/china.json';
import jiangsuJson from '@/assets/json/jiangsu.json';
import guangdongJson from '@/assets/json/guangdong.json';

export default{
    data:function(){
        return {

        }
    },
    mounted:function(){
        this.get_picture1();
        this.get_picture2();
        this.get_picture3();
        echarts.registerMap('china',chinaJson);
        this.get_picture4();
        echarts.registerMap('jiangsu',jiangsuJson);
        this.get_picture5();
        echarts.registerMap('guangdong',guangdongJson);
        this.get_picture6();
        this.get_picture7();
        this.get_picture8();
    },
    methods:{
        get_picture1(){
            axios.get("http://127.0.0.1:12345/picture1").then(
                response =>{
                    var data = response.data;
                    var year = data.year;
                    var value = data.value;
                    var zzl = data.zzl;
                    // console.log(year);
                    // console.log(value);
                    // console.log(zzl);
                    var myChart = echarts.init(document.getElementById('Picture1'));
                    var option = get_picture1_option(year,value,zzl);
                    myChart.setOption(option);
                },
                error =>{
                    console.log(error);
                }
            )
        },
        get_picture2(){
          axios.get("http://127.0.0.1:12345/picture2").then(
                response =>{
                    var data = response.data;
                    var name = data.name;
                    var value = data.value;
                    // console.log(name);
                    // console.log(value);
                    var type_data = [];
                    for(var i=0;i<name.length;i++){
                      type_data.push({value:value[i],name:name[i]});
                    }
                    // console.log(type_data);
                    var myChart = echarts.init(document.getElementById('Picture2'));
                    var option = get_picture2_option(type_data);
                    myChart.setOption(option);
                },
                error =>{
                    console.log(error);
                }
            )
        },
        get_picture3(){
          axios.get("http://127.0.0.1:12345/picture3").then(
                response =>{
                    var data = response.data;
                    var skill_name = data.name;
                    var skill_value = data.value;
                    // console.log(skill_name);
                    // console.log(skill_value);
                    var colorList = [];
                    var color = ['#4B96F3', '#10C6A6', '#F2AF4B', '#FF4D4F', '#AA7AF1'];
                    for (var i = 0; i < skill_name.length; i++) {
                        if (i <= 4) {colorList[i] = color[i]} 
                        else {colorList[i] = color[i % 5]}
                    }
                    var data_new = [];
                    for (i = 0; i < skill_name.length; i++) {
                        data_new.push({
                            value: skill_value[i],
                            name: skill_name[i],
                            itemStyle: {
                                color: colorList[i]
                            }
                        })
                    }
                    // console.log(data_new);
                    var myChart = echarts.init(document.getElementById('Picture3'));
                    var option = get_picture3_option(data_new);
                    myChart.setOption(option);
                },
                error =>{
                    console.log(error);
                }
            )
        },
        get_picture4(){
          axios.get("http://127.0.0.1:12345/picture4").then(
            response =>{
              var data = response.data;
              // console.log(data);
              var province = data.name;
              var value = data.value;
              // console.log(province);
              // console.log(value);
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
        get_picture5(){
          axios.get("http://127.0.0.1:12345/picture5").then(
            response =>{
              var data = response.data;
              // console.log(data);
              var city = data.name;
              var value = data.value;
              // console.log(city);
              // console.log(value);
              var jiangsu_data = [];
              for(var i=0;i<city.length;i++){
                  jiangsu_data.push({value:value[i],name:city[i]});
              }
              var myChart = echarts.init(document.getElementById("Picture5"));
              var option = get_picture5_option(jiangsu_data);
              myChart.setOption(option);
            }
          )
        },
        get_picture6(){
          axios.get("http://127.0.0.1:12345/picture6").then(
            response =>{
              var data = response.data;
              // console.log(data);
              var city = data.name;
              var value = data.value;
              // console.log(city);
              // console.log(value);
              var guangdong_data = [];
              for(var i=0;i<city.length;i++){
                guangdong_data.push({value:value[i],name:city[i]});
              }
              var myChart = echarts.init(document.getElementById("Picture6"));
              var option = get_picture6_option(guangdong_data);
              myChart.setOption(option);
            }
          )
        },
        get_picture7(){
          axios.get("http://127.0.0.1:12345/picture7").then(
            response =>{
              var data = response.data;
              // console.log(data);
              var degree = data.name;
              var salary = data.value;
              // console.log(degree);
              // console.log(salary);
              var degree_data = [];
              for(var i=0;i<degree.length;i++){
                degree_data.push([degree[i],salary[i]]);
              }
              // console.log(degree_data);
              var myChart = echarts.init(document.getElementById("Picture7"));
              var option = get_picture7_option(degree_data);
              myChart.setOption(option);
            }
          )
        },
        get_picture8(){
          axios.get("http://127.0.0.1:12345/picture8").then(
            response =>{
              var data = response.data;
              // console.log(data);
              var experience = data.name;
              var salary = data.value;
              // console.log(degree);
              // console.log(salary);
              var experience_data = [];
              for(var i=0;i<experience.length;i++){
                experience_data.push([experience[i],salary[i]]);
              }
              // console.log(degree_data);
              var myChart = echarts.init(document.getElementById("Picture8"));
              var option = get_picture8_option(experience_data);
              myChart.setOption(option);
            }
          )
        }
    }
}

// 图1：物联网行业市场经济规模和增长率（柱状图+折线图）
function get_picture1_option(year,value,zzl){
    var option = {
                  title:{
                    text:'市场经济规模和增长率',
                    top:'',
                    left:'20px',
                    textStyle:{
                      color:'#FEFEFE',
                      fontSize:16,
                    },
                  },
                  tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'cross',
                    crossStyle: {color: '#999'}
                    }
                  },
                  toolbox: {
                    feature: {
                      dataView: { show: false, readOnly: false },
                      magicType: { show: true, type: ['line', 'bar'] },
                      restore: { show: true },
                      saveAsImage: { show: true }
                    },
                    iconStyle:{
                      color:'#FEFEFE',
                    },
                  },
                  legend: {
                    data: ['经济规模','增长率'],
                    left:'110px',
                    top:'26px',
                    textStyle:{
                      color:'#FEFEFE'
                    }
                  },
                  xAxis: [{
                      type: 'category',
                      data: year,
                      axisPointer: {type: 'shadow'},
                      axisLabel: {
                        color: '#FEFEFE',
                        // fontSize: 12,
                      },
                  }],
                  yAxis: [
                    {
                      type: 'value',
                      name: '经济规模',
                      min: 0,
                      max: 5,
                      interval: 1,
                      nameTextStyle:{
                        color:'#FEFEFE',
                      },
                      axisLabel: {
                        formatter: '{value}',
                        color: '#FEFEFE'
                      }, 
                    },
                    {
                      type: 'value',
                      name: '增长率',
                      min: 0,
                      max: 30,
                      interval: 5,
                      nameTextStyle:{
                        color:'#FEFEFE',
                      },
                      axisLabel: {
                        formatter: '{value}%',
                        color: '#FEFEFE'
                      }
                    }
                  ],
                  series: [
                    {
                      name: '经济规模',
                      type: 'bar',
                      tooltip: {
                        valueFormatter: function (value) {
                        return value;
                        }
                      },
                      data: value
                    },
                    {
                      name: '增长率',
                      type: 'line',
                      yAxisIndex: 1,
                      tooltip: {
                        valueFormatter: function (value) {
                        return value + ' %';
                        }
                      },
                      data: zzl
                    }
                  ]
                };
    return option;              
}

// 图2：物联网行业相关岗位领域分布（饼图）
function get_picture2_option(type_data){
    var option = {
                  title:{
                    text:'岗\n位\n领\n域\n分\n布',
                    left:'10px',
                    top:'10px',
                    textStyle:{
                      color:"#FEFEFE",
                      fontSize:16,
                    }
                  },
                  grid:{
                    containLabel:true,
                    left: '5%',
                    right: '5%',
                    bottom: '5%',
                  },
                  tooltip: {
                    trigger: 'item',
                    axisPointer: {
                      type: 'cross',
                      crossStyle: {color: '#999'}
                    },
                    formatter: '{a} <br/>{b} : ({d}%)',
                  },
                  legend: {
                    top: '76%',
                    textStyle:{
                      color:'#FEFEFE',
                    }
                  },
                  toolbox: {
                    show: true,
                    feature: {
                      mark: { show: true },
                      dataView: { show: true, readOnly: false },
                      restore: { show: true },
                      saveAsImage: { show: true }
                    },
                    iconStyle:{
                      color:'#FEFEFE',
                    },
                  },
                  series: [
                    {
                      name: 'Nightingale Chart',
                      type: 'pie',
                      radius: '50%',
                      center: ['50%', '40%'],
                      roseType: 'area',
                      itemStyle: {
                        borderRadius: 8
                      },
                      data: type_data
                    }
                  ]
                };
      return option;
}

// 图3：物联网行业就业技术需求占比（树形图）
function get_picture3_option(data_new){
  var option = {
                title:{
                  text:'行\n业\n就\n业\n技\n术\n需\n求\n占\n比',
                  top:'10px',
                  left:'--5px',
                  textStyle:{
                    color:'#FEFEFE',
                    fontSize:17,
                  },
                },
                toolbox: {
                    feature: {
                      // dataView: { show: true, readOnly: false },
                      // magicType: { show: true, type: ['line', 'bar'] },
                      restore: { show: true },
                      // saveAsImage: { show: true }
                    }
                  },
                series: [{
                    type: 'treemap',
                    width:'93%',
                    height:'95%',
                    right:'0',
                    breadcrumb: {
                        show: false
                    },
                    label: {
                      show: true,
                      textStyle: {
                          color: '#fff',
                          fontSize: 16,
                      },
                    },
                    itemStyle: {
                      show: true,
                      borderWidth: 1,
                      borderColor: '#fff',
                    },
                    emphasis: {
                            label: {
                                show: true
                            }
                        },
                    data: data_new
                }]
            };
      return option;
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

// 图5：物联网行业企业江苏分布（地图）
function get_picture5_option(jiangsu_data){
  var option = {
    title:{
      text:'江\n苏\n省\n物\n联\n网\n行\n业\n就\n业\n分\n布',
      right:'15px',
      textStyle:{
        color:'#FEFEFE',
        fontSize:16,
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
        {start:60},
        {start:50,end:60},
        {start:30,end:50},
        {start:20,end:30},
        {start:10,end:20},
        {start:4,end:10},
        {start:2,end:4},
        {start:1,end:2},
        {start:0,end:1}
      ],
      color: ['#de1c31','#FF0000','#FF4500','#FFA500','#f1ca17',
        '#f8df72','#1275b6','#2177b9','#abd9e9'],
    },
    series:[
      {
        name:'江苏省分布',
        type:'map',
        map: 'jiangsu',
        zoom: 1.4,
        roam: true,
        itemStyle:{
          normal:{
            label:{show:true,textStyle:{color:"rgb(249, 249, 249)"}}
          }
        },
        emphasis:{
          label:{show:true},
        },
        data:jiangsu_data
      }
    ]
  }
  return option;
}

// 图6：物联网行业企业广东分布（地图）
function get_picture6_option(guangdong_data){
  var option = {
    title:{
      text:'广\n东\n省\n物\n联\n网\n行\n业\n企\n业\n分\n布',
      right:'10px',
      textStyle:{
        color:'#FEFEFE',
        fontSize:16,
      },
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
        {start:170},
        {start:50,end:170},
        {start:20,end:50},
        {start:15,end:20},
        {start:10,end:15},
        {start:4,end:10},
        {start:2,end:4},
        {start:1,end:2},
        {start:0,end:1}
      ],
      color: ['#de1c31','#FF0000','#FF4500','#FFA500','#f1ca17',
        '#f8df72','#1275b6','#2177b9','#abd9e9'],
    },
    series:[
      {
        name:'广东省分布',
        type:'map',
        map: 'guangdong',
        zoom: 1.4,
        roam: true,
        itemStyle:{
          normal:{
            label:{show:true,textStyle:{color:"rgb(249, 249, 249)"}}
          }
        },
        emphasis:{
          label:{show:true},
        },
        data:guangdong_data
      }
    ]
  }
  return option;
}

// 图7：物联网行业学历与薪资的关系（散点图）
function get_picture7_option(degree_data){
    var data = degree_data;
    // console.log(data);
    var option = {
      title:{
        text:'薪资与学历的关系',
        top:'20px',
        left:'10px',
        textStyle:{
          color:'#FEFEFE',
        },
      },
      grid: {
        left: '3%',
        right: '3%',
        bottom: '1%',
        containLabel: true
      },
      tooltip: {
        showDelay: 0,
        formatter: function (params) {
          if (params.value.length > 1) {
            return (
              params.value[0] +
              '：' +
              params.value[1] +
              '元 '
            );
          } else {
            return (
              params.name +
              ' : ' +
              params.value +
              '元 '
            );
          }
        },
        axisPointer: {
          show: true,
          // type: 'cross',
          lineStyle: {
            type: 'dashed',
            width: 1
          }
        }
      },
      toolbox: {
        top:'20px',
        right:'7px',
        feature: {
          dataZoom: {},
          brush: {
            type: ['rect', 'polygon', 'clear']
          }
        },
        iconStyle:{
          color:'#FEFEFE'
        },
      },
      brush: {},
      xAxis: [
        {
          type: 'category',
          // scale: true,
          data: ['初中及以下','中技/中专','高中','大专','本科','硕士','博士'],
          splitLine: {
            show: false
          },
          axisLabel:{
            rotate:25,
            color:'#FEFEFE',
            fontSize:10,
          }
        }
      ],
      yAxis: [
        {
          type: 'value',
          scale: true,
          axisLabel: {
            formatter: '{value} 元',
            color:'#FEFEFE',
            fontSize:10,
          },
          splitLine: {
            show: true,
            interval:30
          }
        }
      ],
      series:[
        {
          type:'scatter',
          emphasis:{
            focus:'series'
          },
          // itemStyle:{
          //   color:'#2775b6',
          // },
          colorBy:'category',
          data:data,
        }
      ]
    }
    return option;
}

// 图8：物联网行业经验与薪资的变化（散点图）
function get_picture8_option(experience_data){
  var data = experience_data;
    console.log(data);
    var option = {
      title:{
        text:'薪资与工作经验的关系',
        top:'22px',
        left:'10px',
        textStyle:{
          color:'#FEFEFE',
        }
      },
      grid: {
        left: '3%',
        right: '3%',
        bottom: '1%',
        containLabel: true
      },
      tooltip: {
        showDelay: 0,
        formatter: function (params) {
          if (params.value.length > 1) {
            return (
              params.value[0] +
              '：' +
              params.value[1] +
              '元 '
            );
          } else {
            return (
              params.name +
              ' : ' +
              params.value +
              '元 '
            );
          }
        },
        axisPointer: {
          show: true,
          // type: 'cross',
          lineStyle: {
            type: 'dashed',
            width: 1
          }
        }
      },
      toolbox: {
        top:'20px',
        right:'7px',
        feature: {
          dataZoom: {},
          brush: {
            type: ['rect', 'polygon', 'clear']
          }
        },
        iconStyle:{
          color:'#FEFEFE'
        }
      },
      brush: {},
      xAxis: [
        {
          type: 'category',
          // scale: true,
          data: ['无需经验','1年','1-2年','2年','1-3年','2-3年','3-4年',
                        '3-5年','3-6年','3-9年','4-6年','5-7年','5-8年','5-10年',
                        '8-9年','1年及以上','2年及以上','3年及以上','4年及以上',
                        '5年及以上','6年及以上','8年及以上','10年及以上'],
          splitLine: {
            show: false
          },
          axisLabel:{
            rotate:45,
            color:'#FEFEFE',
            fontSize:10
          }
        }
      ],
      yAxis: [
        {
          type: 'value',
          scale: true,
          axisLabel: {
            formatter: '{value} 元',
            color:'#FEFEFE',
          },
          splitLine: {
            show: false,
            interval:30
          }
        }
      ],
      series:[
        {
          type:'scatter',
          emphasis:{
            focus:'series'
          },
          data:data,
          // itemStyle:{
          //   color:'#2775b6',
          // },
          colorBy:'category',
        }
      ]
    }
    return option;
}

</script>

