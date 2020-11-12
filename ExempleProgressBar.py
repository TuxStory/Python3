#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import functools
import random
import sys
import time

import progressbar

examples = []

non_interactive_sleep_factor = 100


def sleep(delay):
    '''Make non-interactive examples faster by a factor'''
    if __name__ != '__main__':
        delay /= non_interactive_sleep_factor
    time.sleep(delay)


def example(fn):
    '''Wrap the examples so they generate readable output'''

    @functools.wraps(fn)
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % fn.__name__)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')
            # Sleep a bit to make killing the script easier
            sleep(0.2)

    examples.append(wrapped)
    return wrapped


@example
def with_example_without_stdout_redirection():
    with progressbar.ProgressBar(max_value=10) as progress:
        for i in range(10):
            if i % 3 == 0:
                print('Some print statement %i' % i)
            # do something
            sleep(0.1)
            progress.update(i)


@example
def with_example_stdout_redirection():
    with progressbar.ProgressBar(max_value=10, redirect_stdout=True) as p:
        for i in range(10):
            if i % 3 == 0:
                print('Some print statement %i' % i)
            # do something
            p.update(i)
            sleep(0.1)


@example
def basic_widget_example():
    widgets = [progressbar.Percentage(), progressbar.Bar()]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=10).start()
    for i in range(10):
        # do something
        sleep(0.1)
        bar.update(i + 1)
    bar.finish()


@example
def file_transfer_example():
    widgets = [
        'Test: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker=progressbar.RotatingMarker()),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        # do something
        bar.update(10 * i + 1)
    bar.finish()


@example
def custom_file_transfer_example():
    class CrazyFileTransferSpeed(progressbar.FileTransferSpeed):

        "It's bigger between 45 and 80 percent"

        def update(self, bar):
            if 45 < bar.percentage() < 80:
                return 'Bigger Now ' + progressbar.FileTransferSpeed.update(
                    self, bar)
            else:
                return progressbar.FileTransferSpeed.update(self, bar)

    widgets = [
        CrazyFileTransferSpeed(),
        ' <<<', progressbar.Bar(), '>>> ',
        progressbar.Percentage(),
        ' ',
        progressbar.ETA(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=1000)
    # maybe do something
    bar.start()
    for i in range(200):
        # do something
        bar.update(5 * i + 1)
    bar.finish()


@example
def double_bar_example():
    widgets = [
        progressbar.Bar('>'), ' ',
        progressbar.ETA(), ' ',
        progressbar.ReverseBar('<'),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        # do something
        bar.update(10 * i + 1)
        sleep(0.01)
    bar.finish()


@example
def basic_file_transfer():
    widgets = [
        'Test: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker='0', left='[', right=']'),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=500)
    bar.start()
    # Go beyond the max_value
    for i in range(100, 501, 50):
        sleep(0.1)
        bar.update(i)
    bar.finish()


@example
def simple_progress():
    bar = progressbar.ProgressBar(
        widgets=[progressbar.SimpleProgress()],
        max_value=17,
    ).start()
    for i in range(17):
        sleep(0.1)
        bar.update(i + 1)
    bar.finish()


@example
def basic_progress():
    bar = progressbar.ProgressBar().start()
    for i in range(10):
        sleep(0.1)
        bar.update(i + 1)
    bar.finish()


@example
def progress_with_automatic_max():
    # Progressbar can guess max_value automatically.
    bar = progressbar.ProgressBar()
    for i in bar(range(8)):
        sleep(0.1)


@example
def progress_with_unavailable_max():
    # Progressbar can't guess max_value.
    bar = progressbar.ProgressBar(max_value=8)
    for i in bar((i for i in range(8))):
        sleep(0.1)


@example
def animated_marker():
    bar = progressbar.ProgressBar(
        widgets=['Working: ', progressbar.AnimatedMarker()])
    for i in bar((i for i in range(5))):
        sleep(0.1)


@example
def counter_and_timer():
    widgets = ['Processed: ', progressbar.Counter('Counter: %(value)05d'),
               ' lines (', progressbar.Timer(), ')']
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(15))):
        sleep(0.1)


@example
def format_label():
    widgets = [progressbar.FormatLabel(
        'Processed: %(value)d lines (in: %(elapsed)s)')]
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(15))):
        sleep(0.1)


@example
def animated_balloons():
    widgets = ['Balloon: ', progressbar.AnimatedMarker(markers='.oO@* ')]
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(24))):
        sleep(0.1)


@example
def animated_arrows():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', progressbar.AnimatedMarker(markers='←↖↑↗→↘↓↙')]
        bar = progressbar.ProgressBar(widgets=widgets)
        for i in bar((i for i in range(24))):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')


@example
def animated_filled_arrows():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', progressbar.AnimatedMarker(markers='◢◣◤◥')]
        bar = progressbar.ProgressBar(widgets=widgets)
        for i in bar((i for i in range(24))):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')


@example
def animated_wheels():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Wheels: ', progressbar.AnimatedMarker(markers='◐◓◑◒')]
        bar = progressbar.ProgressBar(widgets=widgets)
        for i in bar((i for i in range(24))):
            sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')


@example
def format_label_bouncer():
    widgets = [
        progressbar.FormatLabel('Bouncer: value %(value)d - '),
        progressbar.BouncingBar(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(100))):
        sleep(0.01)


@example
def format_label_rotating_bouncer():
    widgets = [progressbar.FormatLabel('Animated Bouncer: value %(value)d - '),
               progressbar.BouncingBar(marker=progressbar.RotatingMarker())]

    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(18))):
        sleep(0.1)


@example
def with_right_justify():
    with progressbar.ProgressBar(max_value=10, term_width=20,
                                 left_justify=False) as progress:
        assert progress.term_width is not None
        for i in range(10):
            progress.update(i)


@example
def exceeding_maximum():
    with progressbar.ProgressBar(max_value=1) as progress:
        try:
            progress.update(2)
        except ValueError:
            pass


@example
def reaching_maximum():
    progress = progressbar.ProgressBar(max_value=1)
    try:
        progress.update(1)
    except RuntimeError:
        pass


@example
def stdout_redirection():
    with progressbar.ProgressBar(redirect_stdout=True) as progress:
        print('', file=sys.stdout)
        progress.update(0)


@example
def stderr_redirection():
    with progressbar.ProgressBar(redirect_stderr=True) as progress:
        print('', file=sys.stderr)
        progress.update(0)


@example
def negative_maximum():
    try:
        with progressbar.ProgressBar(max_value=-1) as progress:
            progress.start()
    except ValueError:
        pass


@example
def rotating_bouncing_marker():
    widgets = [progressbar.BouncingBar(marker=progressbar.RotatingMarker())]
    with progressbar.ProgressBar(widgets=widgets, max_value=20,
                                 term_width=10) as progress:
        for i in range(20):
            sleep(0.1)
            progress.update(i)

    widgets = [progressbar.BouncingBar(marker=progressbar.RotatingMarker(),
                                       fill_left=False)]
    with progressbar.ProgressBar(widgets=widgets, max_value=20,
                                 term_width=10) as progress:
        for i in range(20):
            sleep(0.1)
            progress.update(i)


@example
def incrementing_bar():
    bar = progressbar.ProgressBar(widgets=[
        progressbar.Percentage(),
        progressbar.Bar(),
    ], max_value=10).start()
    for i in range(10):
        # do something
        sleep(0.1)
        bar += 1
    bar.finish()


@example
def increment_bar_with_output_redirection():
    widgets = [
        'Test: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker=progressbar.RotatingMarker()),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=1000,
                                  redirect_stdout=True).start()
    for i in range(100):
        # do something
        sleep(0.01)
        bar += 10
        print('Got', i)
    bar.finish()


@example
def eta_types_demonstration():
    widgets = [
        progressbar.Percentage(),
        ' ETA: ', progressbar.ETA(),
        ' Adaptive ETA: ', progressbar.AdaptiveETA(),
        ' Absolute ETA: ', progressbar.AbsoluteETA(),
        ' Adaptive Transfer Speed: ', progressbar.AdaptiveTransferSpeed(),
        ' ', progressbar.Bar(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=500)
    bar.start()
    for i in range(500):
        if i < 100:
            sleep(0.02)
        elif i > 400:
            sleep(0.1)
        else:
            sleep(0.01)
        bar.update(i + 1)
    bar.finish()


@example
def adaptive_eta_without_value_change():
    # Testing progressbar.AdaptiveETA when the value doesn't actually change
    bar = progressbar.ProgressBar(widgets=[
        progressbar.AdaptiveETA(),
        progressbar.AdaptiveTransferSpeed(),
    ], max_value=2, poll_interval=0.0001)
    bar.start()
    for i in range(100):
        bar.update(1)
        sleep(0.1)
    bar.finish()


@example
def iterator_with_max_value():
    # Testing using progressbar as an iterator with a max value
    bar = progressbar.ProgressBar()

    for n in bar(iter(range(100)), 100):
        # iter range is a way to get an iterator in both python 2 and 3
        pass


@example
def eta():
    widgets = [
        'Test: ', progressbar.Percentage(),
        ' | ETA: ', progressbar.ETA(),
        ' | AbsoluteETA: ', progressbar.AbsoluteETA(),
        ' | AdaptiveETA: ', progressbar.AdaptiveETA(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=50).start()
    for i in range(50):
        sleep(0.1)
        bar.update(i + 1)
    bar.finish()


@example
def dynamic_message():
    # Use progressbar.DynamicMessage to keep track of some parameter(s) during
    # your calculations
    widgets = [
        progressbar.Percentage(),
        progressbar.Bar(),
        progressbar.DynamicMessage('loss'),
    ]
    with progressbar.ProgressBar(max_value=100, widgets=widgets) as bar:
        min_so_far = 1
        for i in range(100):
            val = random.random()
            if val < min_so_far:
                min_so_far = val
            bar.update(i, loss=min_so_far)


@example
def format_custom_text():
    format_custom_text = progressbar.FormatCustomText(
        'Spam: %(spam).1f kg, eggs: %(eggs)d',
        dict(
            spam=0.25,
            eggs=3,
        ),
    )

    bar = progressbar.ProgressBar(widgets=[
        format_custom_text,
        ' :: ',
        progressbar.Percentage(),
    ])
    for i in bar(range(25)):
        format_custom_text.update_mapping(eggs=i * 2)
        sleep(0.1)


@example
def simple_api_example():
    bar = progressbar.ProgressBar(widget_kwargs=dict(fill='█'))
    for i in bar(range(200)):
        sleep(0.02)


@example
def ETA_on_generators():
    def gen():
        for x in range(200):
            yield None

    widgets = [progressbar.AdaptiveETA(), ' ',
               progressbar.ETA(), ' ',
               progressbar.Timer()]

    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar(gen()):
        sleep(0.02)


@example
def percentage_on_generators():
    def gen():
        for x in range(200):
            yield None

    widgets = [progressbar.Counter(), ' ',
               progressbar.Percentage(), ' ',
               progressbar.SimpleProgress(), ' ']

    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar(gen()):
        sleep(0.02)


def test(*tests):
    for example in examples:
        if not tests or example.__name__ in tests:
            example()
        else:
            print('Skipping', example.__name__)


if __name__ == '__main__':
    try:
        test(*sys.argv[1:])
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')
