# PyAutoChrome
AutoChrome for Python

- Launcher
    - AutoChrome launch()

- AutoChrome
    - bool wait_condition(condition, timeout)
    - bool wait_conditions([condition_1, condition_2], timeout)
    - {} wait_event(event, timeout)
    - {} wait_lifecycle_event(event, timeout)
    - close

- AutoDom
    - int get_document_id
    - int query_selector(selector)
    - [int] query_selector_all(selector)
    - str get_outer_html(selector)
    - [[number]] get_content_quads(selector)
    - set_attribute_value(selector, name, value)
    - set_outer_html(selector, outer_html)

- AutoInput
    - sendKeys(text)
    - click(selector)
    - click(x, y)
    - drag(slider_button_selector, slider_box_selector)
    - send_tab()
    - send_enter()
    - send_backspace()
    - send_esc()
    - send_left_arrow()
    - send_right_arrow()
    - send_up_arrow()
    - send_down_arrow()
    - send_key_code(code)

- AutoNavigate
    - {} navigate_until_dom_ready(url, timeout)
    - {} navigate_until_dialog_open(url, timeout)
    - {} navigate_until_first_meaning_full_paint(url, timeout)
    - {} navigate_until_lifecycle_event(url, lifecycle_event, timeout)
    - {} navigate_until(url, event, timeout, ref)
    - str navigate_until_network_finished(url, match_url, timeout)
    - {} navigate_until_database_added(url, timeout)

- AutoNetwork
    - clear_browser_cache()
    - clear_browser_cookies()
    - delete_cookies(name, url)
    - delete_cookies(name, domain, path)
    - [cookie] get_all_cookies()
    - [cookie] get_cookies([url])
    - {} get_response_body(request_id)
    - set_blocked_urls([url])
    - set_cache_disabled(cache_disabled)
    - bool set_cookie(name, value, url)
    - set_cookies([cookie_param])
    - set_extra_http_headers((name, value))
    - set_user_agent_override(user_agent)
    - set_ignore_certificate_errors(ignore)

- AutoPage
    - add_script_to_evaluate_on_new_document(java_script)
    - str capture_screen_shot(viewport)
    - str capture_screen_shot()
    - str capture_full_screen_shot()
    - str capture_snapshot()
    - str get_content(url)
    - handle_java_script_dialog(accept, prompt_text)
    - {} navigate(url)
    - {} navigate(url, referrer, transition_type, frame_id)
    - back()
    - forward()
    - reload(ignore_cache, script_to_evaluate_on_load)
    - stop_loading()
    - set_content(html)
    - set_download_behavior(down_load_behavior_type, download_path)
    - str get_frame_id(url)

- AutoRuntime
    - bool eval_until_dialog_or_check_ok(expression, expect_true_exp, timeout)
    - bool eval_until_check_finished(expression, expect_true_exp, expect_false_exp, timeout)
    - {} eval_until_data_received(expression, match_url, timeout)
    - bool eval_until(expression, condition, timeout)
    - bool eval_until(expression, [condition], timeout)
    - {} eval_until(expression, event, timeout, ref)
    - {} eval(expression)
    - {} evaluate(expression)

- AutoWindow
    - bounds get_window_bounds()
    - set_window_bounds(bounds)
    - set_window_bounds(left, top, width, height)
    - set_window_state(window_state)