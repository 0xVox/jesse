from jesse.store import store
import jesse.helpers as jh
import jesse.services.logger as logger


def set_up():
    store.reset()


def test_can_log_info_by_firing_event():
    set_up()

    # fire first info event
    logger.info('first info!!!!!')
    first_logged_info = {'time': jh.now(), 'message': 'first info!!!!!'}

    assert store.logs.info == [first_logged_info]

    # fire second info event
    logger.info('second info!!!!!')
    second_logged_info = {
        'time': jh.now(),
        'message': 'second info!!!!!'
    }

    assert store.logs.info == [first_logged_info, second_logged_info]


def test_can_log_error_by_firing_event():
    set_up()

    # fire first error event
    logger.error('first error!!!!!')
    first_logged_error = {'time': jh.now(), 'message': 'first error!!!!!'}

    assert store.logs.errors == [first_logged_error]

    # fire second error event
    logger.error('second error!!!!!')
    second_logged_error = {'time': jh.now(), 'message': 'second error!!!!!'}

    assert store.logs.errors == [first_logged_error, second_logged_error]
