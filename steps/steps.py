from radish.stepregistry import step
from radish import given, when, then
# from twentyone import *
# backgound
@step('a global administrator named "Greg"')
def a_global_administrator_named_greg(step):
    print('STEP: Given a global administrator named "Greg"')
    raise NotImplementedError(u'STEP: a global administrator named "Greg"')


@step('a blog named "Greg\'s anti-tax rants"')
def a_blog_named_gregs_antitax_rants(step):
    print('STEP: Given a blog named "Greg\'s anti-tax rants"')


@step('a customer named "Wilson"')
def a_customer_named_wilson(step):
    print('STEP: Given a customer named "Wilson"')

@step("scenario 2 description")
def scenario_2_description(step):
    print("This step is not implemented yet")

@step("something else we can check happens too")
def something_else_we_can_check_happens_too(step):
    print("something else we can check happens too")
    # assert(1==0)


@step("scenario outline")
def scenario_outline(step):
    print("scenario outline")
    raise NotImplementedError(u'STEP: scenario outline')

@step("description")
def description(step):
    print("description")

# table comming
@given('the following people exist')
def the_following_people_exist(step):
    step.context.users = step.table
    raise NotImplementedError(u'STEP: the following people exist')


@given('some precondition 1')
def some_precondition_1(step):
    print(u'STEP: Given some precondition 1')


@when('some action by the actor')
def some_action_by_the_actor(step):
    print('STEP: When some action by the actor')


@when('some other action')
def some_other_action(step):
    print('STEP: When some other action')


@then('some testable outcome is achieved')
def some_testable_outcome_is_achieved(step):
    print('STEP: Then some testable outcome is achieved')
    # assert(1==0)


# @then('something else we can check happens too')
# def something_else_we_can_check_happens_too(step):
#     print('STEP: Then something else we can check happens too')
#     # assert(1==0)

# @step("something else we can check happens too")
# def something_else_we_can_check_happens_too(step):
#     print("And something else we can check happens too")


# scenario 2
@given('some precondition')
def some_precondition(step):
    # print('STEP: Given some precondition')
    1+1
    # step.skip()

#step text data
@given('some other precondition with doc string')
def some_other_precondition_with_doc_string(step):
    1+1
    # step.skip()
    # step.context.quote = step.text
    # print('STEP: Given some other precondition with doc string')


@when('yet another action')
def yet_another_action(step):
    print('STEP: When yet another action')

# # *
# @given('something else we can check happens too')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given something else we can check happens too')


@step('I don\'t see something else')
def i_dont_see_something_else(step):
    print('STEP: Given I don\'t see something else')
    #step.skip()



# scenario 3
# @given('the cow weighs {weight:g} kg')
# def the_cow_weighs_weight_kg(step, weight):
#     print('STEP: Given the cow weighs kg: ')

@step(r'Given the cow weighs {weight:g} kg')
def the_cow_weighs_weight_kg(step, weight):
    print('STEP: Given the cow weighs kg: ')


@when('we calculate the feeding requirements')
def we_calculate_the_feeding_requirements(step):
    print('STEP: When we calculate the feeding requirements')


@then('the energy should be {energy:g} MJ')
def the_energy_should_be_energy_mj(step, energy):
    # print('STEP: Then the energy should be MJ: ')
    assert(0==0)


# @given(u'a blog named "Greg\'s anti-tax rants"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given a blog named "Greg\'s anti-tax rants"')


# @given(u'the cow weighs 500 kg')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given the cow weighs 500 kg')
#
#
# @then(u'the energy should be 29500 MJ')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the energy should be 29500 MJ')
