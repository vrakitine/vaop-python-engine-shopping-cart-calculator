# V2.0 | The VOAP code Version 1.0 calculates 
# the cost of cart with discount on all cart

####################################################################
### VA-script | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################

class VA_script:
  def __init__(self):
    self.va_script = {"d":"All VA-scripts", "v":{
			"va_script_00":{"d":"Init VA-script","v":{
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
						  "Direction_10":"Action_10_000", "_010":"Done"
					  },
				  "Action_9010":{
						  "_agent_position":{
							  "en-US":"test jump back from Action_10_XXX",
							  "ru-RU":""
						  },
						  "_action_description":{
							  "_010":"empty"
						  },
						  "Direction_10":"Action_END", "_010":"Done"
					  }
				  }
							
				},
			"va_script_10":{"d":"The group of Actions for testing","v":{
				  "Action_10_000":{
						  "_agent_position":{
							  "en-US":"In Init block of VA-box",
							  "ru-RU":"В блоке Init VA-box"
						  },
						  "_action_description":{
							  "_010":"--> init action"
						  },
						  "Direction_10":"Action_10_010",  "_010":"Done"
					  },
				  "Action_10_010":{
						  "_agent_position":{
							  "en-US":"Action_10_010 jupm to Action_10_020",
							  "ru-RU":""
						  },
						  "_action_description":{
							  "_010":"empty"
						  },
						  "Direction_10":"Action_10_020", "_010":""
					  },
				  "Action_10_020":{
						  "_agent_position":{
							  "en-US":"Action_10_010 jupm to Action_9010",
							  "ru-RU":""
						  },
						  "_action_description":{
							  "_010":"empty"
						  },
						  "Direction_10":"Action_9010", "_010":""
					  }
					}
				}
			}
    }
  def getVaScript(self, va_data):

    return self.va_script['v'][va_data['va']['script_group_code']['v']]['v']

  def getAllActionCodes(self):
    temp = []
    for temp_1 in self.va_script['v'].keys():
      for temp_2 in self.va_script['v'][temp_1]['v'].keys():
        temp.append(temp_2)

    return temp

	
####################################################################
### VA-script | End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
####################################################################

####################################################################
### Actions Classes | Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
####################################################################
class Items:
  def __init__(self):
    self.items = {"d":"Items in online store [dictionary]", "v":{
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

  def getAll(self):

    return self.items  

  def getCostByItemId(self, temp):

    return self.items['v'][temp]['v']['attr']['v']['cost']  

class Cart:
  def __init__(self):
    self.items_in_cart = {"d":"Items in cart [array]", "v":[
        {"item_id":{"d":"Item id","v":"98"},"item_q":{"d":"Item quantity","v":4}},
        {"item_id":{"d":"Item id","v":"560"},"item_q":{"d":"Item quantity","v":1}},
        {"item_id":{"d":"Item id","v":"34"},"item_q":{"d":"Item quantity","v":2}}  
      ]}

  def getAll(self):

    return self.items_in_cart

  def GetQuantityOfItemByNumberInList(self, temp):

    return self.items_in_cart['v'][temp]['item_q']

  def GetItemIdOfItemByNumberInList(self, temp):

    return self.items_in_cart['v'][temp]['item_id']
"""
class Discount:
  def __init__(self):
    self.discount = {"d":"Items in online store [dictionary]", "v":{
        "cart_discount":{"d":"The discount on all cart","v":{
            "1":{"d":"Discount id","v":{
                "is_available":{"d":"Is this discount available[True/False",True:},
                "max_cost":{"d":"Use this discount if cost of cart more than 'max_cost","v":100},
                "discounts":{"d":"Discounts","v":{
                    'discount_types':{"d":"Discount types[Amount,%, free shipping, ...","v":{
                        'amount':{"d':}
                    }}}
                
                }
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
"""
class Actions:
  
  ### Action_000 ###################################################
  def Action_000(va_data):

    ### Start | Init setting
   
    va_data['log'] = {}
    va_data['log'] = {"d":"For log", "v":{"title":{"d":"For title", "v":"unknown_title"},
                                          "value":{"d":"For value", "v":""}
                                          }}

    va_data['items_in_cart'] = va_data['cart_instance']['v'].getAll()

    va_data['items'] = va_data['items_instance']['v'].getAll()

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

    va_data['item_q_020'] = va_data['cart_instance']['v'].GetQuantityOfItemByNumberInList(va_data['i']['v'])
    va_data['custom_log']['v'].append('item_q_020')

    va_data['item_id_020'] = va_data['cart_instance']['v'].GetItemIdOfItemByNumberInList(va_data['i']['v'])
    va_data['custom_log']['v'].append('item_id_020')

    va_data['cost_020'] = va_data['items_instance']['v'].getCostByItemId(va_data['item_id_020']['v'])
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
  ### Action_9010 ###################################################
  def Action_9010(va_data):

    va_data['va']['direction']['v'] = "Direction_10" 

    return va_data

  ### Action_10_000 ###################################################
  def Action_10_000(va_data):
 
    va_data['va']['direction']['v'] = "Direction_10" 

    return va_data    
  ### Action_10_010 ###################################################
  def Action_10_010(va_data):
    
    va_data['va']['direction']['v'] = "Direction_10" 

    return va_data    
  ### Action_10_020 ###################################################
  def Action_10_020(va_data):
    
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

    va_data['va']['script_group_code'] = {}
    va_data['va']['script_group_code']['v'] = 'va_script_00'
    va_data['va']['script_group_code']['d'] = "The script group code"
	
    va_data['va']['script_instance'] = {}
    va_data['va']['script_instance']['v'] = VA_script()
    va_data['va']['script_instance']['d'] = "VA script instance"

    va_data['va']['previous_script'] = {}
    va_data['va']['previous_script']['v'] = va_data['va']['script_instance']['v'].getVaScript(va_data)
    va_data['va']['previous_script']['d'] = "previous VA script"

    va_data['va']['script'] = {}
    va_data['va']['script']['v'] = va_data['va']['script_instance']['v'].getVaScript(va_data)
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
      va_data['va']['tracking_actions']['v'] = va_data['va']['script_instance']['v'].getVaScript(va_data).keys()
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
        print("\n\n -----------> Error: Looping")
        break

      va_data = VA_box_tools.getAction(va_data)

      if va_data['va']['is_tracking_on']['v'] and (va_data['va']['previous_action']['v'] in va_data['va']['script_instance']['v'].getAllActionCodes()):
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
  def getAction(va_data):
    temp_script_group_code = va_data['va']['script_group_code']['v']

    temp_action = va_data['va']['script']['v'][va_data['va']['current_action']['v']][va_data['va']['direction']['v']]
    va_data['va']['previous_action']['v'] = va_data['va']['current_action']['v']
    va_data['va']['current_action']['v'] = temp_action  

    temp = va_data['va']['current_action']['v'].split('_')

    if len(temp) == 2 or len(temp) == 3:
      if len(temp) == 2:
        va_data['va']['script_group_code']['v'] = 'va_script_00'
      if len(temp) == 3:
        va_data['va']['script_group_code']['v'] = 'va_script_' + temp[1]

      va_data['va']['previous_script']['v'] = va_data['va']['script']['v']
      va_data['va']['script']['v'] = va_data['va']['script_instance']['v'].getVaScript(va_data)   
    else:
      print("Error in getAction -> unknown Action code:[" + va_data['va']['current_action'])

    if va_data['va']['is_tracking_on']['v']:
      if temp_script_group_code != va_data['va']['script_group_code']['v']:
        print(">>> The v-agent had jumped from group [" + temp_script_group_code + "] to group [" + va_data['va']['script_group_code']['v'] + "]\n")

    return va_data

  def isNotDefinedOutsideOfVaBox(var_array, var_key_name):
    temp = True
    if var_key_name in var_array:
      if ('v' in var_array[var_key_name]) and ('d' in var_array[var_key_name]):
        temp = False

    return temp

  def getAgentPosition(va_data):
    va_data['va']['agent_position']['v'] = "Now in [" + va_data['va']['previous_action']['v'] + "]"
    if '_agent_position' in va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]:
      if va_data['va']['locale_lang_code']['v'] in va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
        va_data['va']['agent_position']['v'] = va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position'][va_data['va']['locale_lang_code']['v']]
        if va_data['va']['agent_position']['v'] == '':
          if va_data['va']['locale_lang_code_defaulf']['v'] in va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
            va_data['va']['agent_position']['v'] = va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position'][va_data['va']['locale_lang_code_defaulf']['v']]
      if va_data['va']['locale_lang_code']['v'] not in va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
        if va_data['va']['locale_lang_code_defaulf']['v'] in va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position']:
          va_data['va']['locale_lang_code']['v'] = va_data['va']['previous_script']['v'][va_data['va']['previous_action']['v']]['_agent_position'][va_data['va']['locale_lang_code_defaulf']['v']]
    
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

va_data['cart_instance'] = {'d':"The instance of the Сart class",'v':Cart()}
va_data['items_instance'] = {'d':"The instance of the Items class",'v':Items()}

### Start the setting for log and tracking options ################
va_data['va'] = {"is_tracking_on":{"d":"Is tracing ON?? (True/False)","v":True}}

"""
va_data['va']['tracking_actions'] = {}
va_data['va']['tracking_actions']['v'] = ['Action_010']
va_data['va']['tracking_actions']['d'] = "The list of actions to track"

va_data['va']['jump_pause_after_actions'] = {}
va_data['va']['jump_pause_after_actions']['v'] = ['Action_010']
va_data['va']['jump_pause_after_actions']['d'] = "The jump pause after actions"
"""
### End the setting for log and tracking options ##################


va_data = VA_box.start(va_data)

print(va_data['total_cost'])
print('\nThe end')

