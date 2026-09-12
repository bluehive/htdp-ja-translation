-- Page breaks for HTDP JA builds. Canonical rules: BUILD.md
-- 本文: break before # and ## (章・節).
-- 付録: break before any heading whose title contains 「付録」(付録ごと).
--        Do not break on other ## / ### inside an appendix.
local in_appendix = false

local function break_blocks()
  if FORMAT:match('typst') then
    return { pandoc.RawBlock('typst', '#pagebreak()') }
  elseif FORMAT:match('latex') then
    return { pandoc.RawBlock('latex', '\\clearpage') }
  else
    return { pandoc.RawBlock('html', '<div class="pagebreak"></div>') }
  end
end

function Header(el)
  local title = pandoc.utils.stringify(el)
  if title:find('付録', 1, true) then
    in_appendix = true
    local out = break_blocks()
    table.insert(out, el)
    return out
  end
  if el.level == 1 then
    in_appendix = false
    local out = break_blocks()
    table.insert(out, el)
    return out
  end
  if el.level == 2 and not in_appendix then
    local out = break_blocks()
    table.insert(out, el)
    return out
  end
  return el
end
