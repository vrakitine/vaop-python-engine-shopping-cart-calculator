## 2021_12_22__000 Article - VAOP and Shopping Cart calculator

####################################################################
### VA-script | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_script:
  def getVaScript():
    va_script = {
    "Action_000":{
        "_agent_position":{
            "en-US":"In Init block of VA-box",
            "ru-RU":"В блоке Init VA-box"
        },
        "_action_description":{
            "_010":"--> init action"
        },
        "Direction_10":"Action_010",  "_010":"Done"
    },
"Action_010":{
        "_agent_position":{
            "en-US":"The v-agent is checking the end of array of items",
            "ru-RU":"Это конец массива элементов с покупками"
        },
        "_action_description":{
            "_010":"empty"
        },
        "Direction_10":"Action_020", "_010":"",
        "Direction_20":"Action_9000", "_010":""
    },
"Action_020":{
        "_agent_position":{
            "en-US":"The v-agent is taking the next item and adding the cost of this items to va_data['total_cost']",
            "ru-RU":"V-agent берет следующий элемент и добавляет стоимость этого элемента в va_data ['total_cost']"
        },
        "_action_description":{
            "_010":"empty"
        },
        "Direction_10":"Action_010",  "_010":""
    },
"Action_9000":{
        "_agent_position":{
            "en-US":"The v-agent found the end of array of items in the shopping cart",
            "ru-RU":"V-agent обнаружил конец массива товаров в корзине."
        },
        "_action_description":{
            "_010":"empty"
        },
        "Direction_10":"Action_END", "_010":"Done"
    }
}

    return va_script
####################################################################
### VA-script | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################

####################################################################
### Actions Classes | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################
class Actions:
  
  ### Action_000 ###################################################
  def Action_000(va_data):

    ### Start | Init setting
   
    va_data['log'] = {}
    va_data['log'] = {"d":"For log", "v":{"title":{"d":"For title", "v":"unknown_title"},
                                          "value":{"d":"For value", "v":""}
                                          }}

    va_data['items_in_cart'] = {"d":"Items in cart [array]", "v":[
        {"item_id":{"d":"Item id","v":"98"},"item_q":{"d":"Item quantity","v":4}},
        {"item_id":{"d":"Item id","v":"560"},"item_q":{"d":"Item quantity","v":1}},
        {"item_id":{"d":"Item id","v":"34"},"item_q":{"d":"Item quantity","v":2}}  
      ]}

    va_data['items'] = {"d":"Items in online store [dictionary]", "v":{
        "34":{"d":"Item id","v":{
            "attr":{"d":"Attributes of item","v":{
                "name":{"d":"Name of item","v":"Name_34"},
                "cost":{"d":"The cost of item","v":3.4},
                "department_id":{"d":"Department id","v":"10"}
            }}
        }},
        "98":{"d":"Item id","v":{
            "attr":{"d":"Attributes of item","v":{
                "name":{"d":"Name of item","v":"Name_98"},
                "cost":{"d":"The cost of item","v":9.8},
                "department_id":{"d":"Department id","v":"10"}
            }}
        }},
        "560":{"d":"Item id","v":{
            "attr":{"d":"Attributes of item","v":{
                "name":{"d":"Name of item","v":"Name_560"},
                "cost":{"d":"The cost of item","v":5.60},
                "department_id":{"d":"Department id","v":"10"}
            }}
        }},
    }}  

    va_data['total_cost'] = {"d":"The TotalCost of the items in the Cart","v":0}

    va_data['i'] = {"d":"Index in Items in cart","v":-1}

    va_data['max_index'] = {
        "d":"Max index in Items in cart",
        "v":len(va_data['items_in_cart']['v']) - 1
        }

    va_data['custom_log'] = {}
    va_data['custom_log']['v'] = [] 
    va_data['custom_log']['d'] = "This is the log array for tracking custom variables in actions."

    """
    va_data[''] = {}
    va_data['']['v'] = 0
    va_data['']['d'] = "Empty"
    """
    ### End | Init setting

     

    va_data['va']['direction']['v'] = "Direction_10"

    return va_data

  ### Action_010 ###################################################
  def Action_010(va_data):
    va_data['va']['direction']['v'] = "Direction_10"

    va_data['i']['v'] += 1
    if va_data['i']['v'] > va_data['max_index']['v']:
      va_data['i']['v'] -= 1
      va_data['va']['direction']['v'] = "Direction_20"

    ### for log
    va_data['custom_log']['v'].append('i')
    va_data['custom_log']['v'].append('max_index')

    return va_data

  ### Action_020 ###################################################
  def Action_020(va_data):

    temp__i = va_data['i']['v'] 

    va_data['item_q_020'] = {}
    va_data['item_q_020']['v'] = va_data['items_in_cart']['v'][temp__i]['item_q']['v']
    va_data['item_q_020']['d'] = va_data['items_in_cart']['v'][temp__i]['item_q']['d'] 
    
    va_data['custom_log']['v'].append('item_q_020')

    va_data['item_id_020'] = {}
    va_data['item_id_020']['v'] = va_data['items_in_cart']['v'][temp__i]['item_id']['v']
    va_data['item_id_020']['d'] = va_data['items_in_cart']['v'][temp__i]['item_id']['d'] 

    va_data['custom_log']['v'].append('item_id_020')

    va_data['cost_020'] = {}
    va_data['cost_020']['v'] = va_data['items']['v'][va_data['item_id_020']['v']]['v']['attr']['v']['cost']['v']
    va_data['cost_020']['d'] = va_data['items']['v'][va_data['item_id_020']['v']]['v']['attr']['v']['cost']['d'] 

    va_data['custom_log']['v'].append('cost_020')

    va_data['total_cost']['v'] += va_data['cost_020']['v'] * va_data['item_q_020']['v']
    va_data['custom_log']['v'].append('total_cost')

    va_data['va']['direction']['v'] = "Direction_10"

    ### for log

    #va_data['custom_log']['v'].append({"d":, "v":})


    return va_data

  ### Action_9000 ###################################################
  def Action_9000(va_data):

    va_data['va']['direction']['v'] = "Direction_10" 

    return va_data
####################################################################
### Actions Class | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################

####################################################################
### Actions_tools | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################
class Actions_tools:

  def Action_variables_tracking_row(va_data):
    print(">>> custom_log -->")
    if len(va_data['custom_log']['v']) == 0:
      print("\tEmpty")
    for temp in va_data['custom_log']['v']:
      print("\t" + temp ,"= [" + str(va_data[temp]['v']) + "] <-- " +  va_data[temp]['d'])
    va_data['custom_log']['v'] = []

    return va_data 
####################################################################
### Actions_tools Class | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################

####################################################################
### VA_box | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_box:
  
  def start(va_data):

    ### Start | The VAOP variables setting

    va_data['abbreviations'] = {}
    va_data['abbreviations']['va'] = 'The VAOP variables setting'

    if 'va' not in va_data:
      va_data['va'] = {}
    va_data['va']['jump'] = {}
    va_data['va']['jump']['v'] = 0
    va_data['va']['jump']['d'] = "The sequential number of the v-agent's jump"

    va_data['va']['max_jump'] = {}
    va_data['va']['max_jump']['v'] = 1000
    va_data['va']['max_jump']['d'] = "The max number of the v-agent's jump. It is for prevent looping."

    va_data['va']['locale_lang_code_defaulf'] = {}
    va_data['va']['locale_lang_code_defaulf']['v'] = 'en-US'
    va_data['va']['locale_lang_code_defaulf']['d'] = "The default locale language code"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va'],'locale_lang_code'):
      va_data['va']['locale_lang_code'] = {}
      va_data['va']['locale_lang_code']['v'] = 'en-US'
      va_data['va']['locale_lang_code']['d'] = "The locale language code"

    va_data['va']['agent_position'] = {}
    va_data['va']['agent_position']['v'] = 'Unknown'
    va_data['va']['agent_position']['d'] = "It is info about what is v-agent doing at this moment"

    va_data['va']['script'] = {}
    va_data['va']['script']['v'] = VA_script.getVaScript()
    va_data['va']['script']['d'] = "VA script"

    va_data['va']['previous_action'] = {}
    va_data['va']['previous_action']['v'] = 'Unknown'
    va_data['va']['previous_action']['d'] = "The previous Action"

    va_data['va']['current_action'] = {}
    va_data['va']['current_action']['v'] = 'Action_000'
    va_data['va']['current_action']['d'] = "The current Action"

    va_data['va']['direction'] = {}
    va_data['va']['direction']['v'] = "Direction_10"
    va_data['va']['direction']['d'] = "Direction"

    ### for va-traking
    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va'],'is_tracking_on'):
      va_data['va']['is_tracking_on'] = {}
      va_data['va']['is_tracking_on']['v'] = False
      va_data['va']['is_tracking_on']['d'] = "Is tracking ON? (True/False)"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va'],'content_of_va_tracking_row'):
      va_data['va']['content_of_va_tracking_row'] = {}
      va_data['va']['content_of_va_tracking_row']['v'] = ['jump', 'previous_action', 'direction', 'agent_position']
      va_data['va']['content_of_va_tracking_row']['d'] = "The content of va-tracking row"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va'],'tracking_actions'):
      va_data['va']['tracking_actions'] = {}
      va_data['va']['tracking_actions']['v'] = VA_script.getVaScript().keys()
      va_data['va']['tracking_actions']['d'] = "The list of actions to track"

    if VA_box_tools.isNotDefinedOutsideOfVaBox(va_data['va'],'jump_pause_after_actions'):
      va_data['va']['jump_pause_after_actions'] = {}
      va_data['va']['jump_pause_after_actions']['v'] = []
      va_data['va']['jump_pause_after_actions']['d'] = "The jump pause after actions"


    ### End | The VAOP variables setting
    
    va_data = Actions.Action_000(va_data)
  
    while 1 == 1: 
      va_data['va']['jump']['v'] += 1
      if va_data['va']['jump']['v'] > va_data['va']['max_jump']['v']:
        print(va_data)
        print("\n\n Error: Looping")
        break

      temp = va_data['va']['script']['v'][va_data['va']['current_action']['v']][va_data['va']['direction']['v']]

      va_data['va']['previous_action']['v'] = va_data['va']['current_action']['v']
      va_data['va']['current_action']['v'] = temp  

      if va_data['va']['is_tracking_on']['v'] and (va_data['va']['previous_action']['v'] in va_data['va']['tracking_actions']['v']):
        va_data = VA_box_tools.VA_tracking_row(va_data)
        va_data = Actions_tools.Action_variables_tracking_row(va_data)
        print("\n")
      
      if va_data['va']['current_action']['v'] in va_data['va']['script']['v']:
        if va_data['va']['current_action']['v'] in va_data['va']['jump_pause_after_actions']['v'] and va_data['va']['is_tracking_on']['v'] and (va_data['va']['current_action']['v'] in va_data['va']['tracking_actions']['v']):
          print("jump_pause_after_actions:", va_data['va']['jump_pause_after_actions']['v'])
          temp = input("pause ===> after action:[" + va_data['va']['current_action']['v'] + "] <enter> - continue, <space><enter> - break")
          if temp == ' ':
            break
        va_data['va']['direction']['v'] = 'direction unknown'        
        eval('Actions.' + va_data['va']['current_action']['v'] + "(va_data)")
      else:
        break

    print('The v-agent is finished jumping in the action [', va_data['va']['current_action']['v'], ']')    

    return va_data

class VA_box_tools: ##########################################################
  def isNotDefinedOutsideOfVaBox(var_array, var_key_name):
    temp = True
    if var_key_name in var_array:
      if ('v' in var_array[var_key_name]) and ('d' in var_array[var_key_name]):
        temp = False

    return temp

  def getAgentPosition(va_data):
    va_data['va']['agent_position']['v'] = "Now in [" + va_data['va']['previous_action']['v'] + "]"
    if '_agent_position' in va_data['va']['script']['v'][va_data['va']['previous_action']['v']]:
      if va_data['va']['locale_lang_code']['v'] in va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
        va_data['va']['agent_position']['v'] = va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position'][va_data['va']['locale_lang_code']['v']]
        if va_data['va']['agent_position']['v'] == '':
          if va_data['va']['locale_lang_code_defaulf']['v'] in va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
            va_data['va']['agent_position']['v'] = va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position'][va_data['va']['locale_lang_code_defaulf']['v']]
      if va_data['va']['locale_lang_code']['v'] not in va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
        if va_data['va']['locale_lang_code_defaulf']['v'] in va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
          va_data['va']['locale_lang_code']['v'] = va_data['va']['script']['v'][va_data['va']['previous_action']['v']]['_agent_position'][va_data['va']['locale_lang_code_defaulf']['v']]
    
    return va_data  

  def VA_tracking_row(va_data):
    va_data = VA_box_tools.getAgentPosition(va_data)
    print("va-agent tracking -->")
    for temp in va_data['va']['content_of_va_tracking_row']['v']:
      print("\t" + temp ,"= [" + str(va_data['va'][temp]['v']) + "] <-- " +  va_data['va'][temp]['d'])

    return va_data 
####################################################################
### VA_box | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################


va_data = {}
va_data['va'] = {}

va_data['va'] = {"is_tracking_on":{"d":"Is tracing ON?? (True/False)","v":True}}

"""
va_data['va']['tracking_actions'] = {}
va_data['va']['tracking_actions']['v'] = ['Action_010']
va_data['va']['tracking_actions']['d'] = "The list of actions to track"

va_data['va']['jump_pause_after_actions'] = {}
va_data['va']['jump_pause_after_actions']['v'] = ['Action_010']
va_data['va']['jump_pause_after_actions']['d'] = "The jump pause after actions"
"""

va_data = VA_box.start(va_data)

print("\n" + str(va_data['total_cost']['d']), '[' + str(va_data['total_cost']['v']) + ']')
print('\nThe end')

#va_data['va'] = {}
#print(va_data['va'])
