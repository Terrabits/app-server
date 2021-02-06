from   aiohttp import web
import app_server
import sys
import webbrowser


if __name__ == '__main__':
    args = app_server.command_line.parse()

    app = web.Application()

    # routes
    handler      = app_server.handler.get(args.instr_address, args.instr_port)
    instr_route  = web.get('/instr', handler)

    static_route = web.static('/', args.directory, show_index=True)

    # note instr must be first!??
    routes = [instr_route, static_route]
    app.add_routes(routes)

    # open browser?
    if args.open_browser:
        webbrowser.open_new_tab(f'http://{args.host}:{args.port}')

    # start
    web.run_app(app, host=args.host, port=args.port)
